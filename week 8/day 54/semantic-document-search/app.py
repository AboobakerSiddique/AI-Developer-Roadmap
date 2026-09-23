import os
import tempfile
from pathlib import Path

import streamlit as st
from google import genai

from loader import load_document
from chunker import recursive_split
from embeddings import get_embedding
from vector_store import VectorStore


# --------------------------------------------------
# CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Semantic Document Search",
    page_icon="⌕",
    layout="wide"
)


# --------------------------------------------------
# GEMINI CLIENT
# --------------------------------------------------

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)


# --------------------------------------------------
# VECTOR STORE
# --------------------------------------------------

store = VectorStore()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "indexed" not in st.session_state:
    st.session_state.indexed = False

if "indexed_file" not in st.session_state:
    st.session_state.indexed_file = None

if "chunk_count" not in st.session_state:
    st.session_state.chunk_count = 0


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("Semantic Document Search")

st.caption(
    "Gemini embeddings + ChromaDB + grounded question answering"
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("Document")

    uploaded_file = st.file_uploader(
        "Upload a document",
        type=["pdf", "txt", "md", "docx"]
    )

    if st.session_state.indexed:

        st.success(
            f"Indexed: {st.session_state.indexed_file}"
        )

        st.caption(
            f"{st.session_state.chunk_count} chunks"
        )


# --------------------------------------------------
# DOCUMENT INDEXING
# --------------------------------------------------

if uploaded_file:

    st.write(
        f"**Selected:** `{uploaded_file.name}`"
    )

    if st.button(
        "Index document",
        type="primary"
    ):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=Path(uploaded_file.name).suffix
        ) as temp_file:

            temp_file.write(
                uploaded_file.getvalue()
            )

            temp_path = temp_file.name

        try:

            with st.spinner(
                "Reading and indexing document..."
            ):

                # ------------------------------------------
                # 1. CLEAR PREVIOUS DOCUMENT
                # ------------------------------------------

                store.clear()

                # ------------------------------------------
                # 2. LOAD DOCUMENT
                # ------------------------------------------

                documents = load_document(
                    temp_path
                )

                # ------------------------------------------
                # 3. CHUNK DOCUMENT
                # ------------------------------------------

                all_chunks = []

                for document in documents:

                    chunks = recursive_split(
                        document["content"],
                        chunk_size=500
                    )

                    for chunk_index, chunk in enumerate(
                        chunks
                    ):

                        all_chunks.append({
                            "text": chunk,
                            "source": uploaded_file.name,
                            "chunk_id": chunk_index,
                            "metadata": document["metadata"]
                        })

                if not all_chunks:
                    st.error(
                        "No readable text was found in "
                        "the uploaded document."
                    )

                    st.stop()

                # ------------------------------------------
                # 4. PREPARE DATA
                # ------------------------------------------

                ids = [
                    f"chunk_{index}"
                    for index in range(
                        len(all_chunks)
                    )
                ]

                texts = [
                    chunk["text"]
                    for chunk in all_chunks
                ]

                metadatas = [
                    {
                        "source": chunk["source"],
                        "chunk_id": chunk["chunk_id"],
                        **chunk["metadata"]
                    }
                    for chunk in all_chunks
                ]

                # ------------------------------------------
                # 5. CREATE EMBEDDINGS
                # ------------------------------------------

                embeddings = [
                    get_embedding(text)
                    for text in texts
                ]

                # ------------------------------------------
                # 6. STORE IN CHROMA
                # ------------------------------------------

                store.add_documents(
                    ids=ids,
                    documents=texts,
                    embeddings=embeddings,
                    metadatas=metadatas
                )

                # ------------------------------------------
                # UPDATE SESSION STATE
                # ------------------------------------------

                st.session_state.indexed = True

                st.session_state.indexed_file = (
                    uploaded_file.name
                )

                st.session_state.chunk_count = (
                    len(all_chunks)
                )

            st.success(
                f"Successfully indexed "
                f"{len(all_chunks)} chunks."
            )

        except Exception as error:

            st.error(
                f"Indexing failed: {error}"
            )

        finally:

            # Remove temporary file
            try:
                os.remove(temp_path)
            except OSError:
                pass


# --------------------------------------------------
# SEARCH / QUESTION ANSWERING
# --------------------------------------------------

st.divider()

st.subheader("Ask your document")

if not st.session_state.indexed:

    st.info(
        "Upload a document and index it before "
        "asking a question."
    )

else:

    query = st.text_input(
        "Question",
        placeholder=(
            "e.g. What is the main purpose of "
            "this document?"
        )
    )

    if query:

        with st.spinner(
            "Searching document..."
        ):

            # ------------------------------------------
            # 1. EMBED QUESTION
            # ------------------------------------------

            query_embedding = get_embedding(
                query
            )

            # ------------------------------------------
            # 2. RETRIEVE TOP-K CHUNKS
            # ------------------------------------------

            results = store.search(
                query_embedding,
                top_k=3
            )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        # ------------------------------------------
        # 3. BUILD CONTEXT
        # ------------------------------------------

        context_parts = []

        for index, document in enumerate(
            documents
        ):

            metadata = metadatas[index]

            source = metadata.get(
                "source",
                "Unknown"
            )

            page = metadata.get(
                "page"
            )

            if page:
                location = (
                    f"{source}, Page {page}"
                )
            else:
                location = source

            context_parts.append(
                f"[Source: {location}]\n"
                f"{document}"
            )

        context = "\n\n---\n\n".join(
            context_parts
        )

        # ------------------------------------------
        # 4. ASK GEMINI
        # ------------------------------------------

        prompt = f"""
You are a document question-answering assistant.

Answer the user's question using ONLY the
provided document context.

If the answer cannot be found in the context,
say:

"I couldn't find that information in the document."

Do not invent information.

Keep the answer concise and directly answer
the question.

DOCUMENT CONTEXT:
----------------

{context}

----------------

USER QUESTION:
{query}
"""

        with st.spinner(
            "Generating grounded answer..."
        ):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

        # ------------------------------------------
        # 5. DISPLAY ANSWER
        # ------------------------------------------

        st.subheader("Answer")

        st.write(
            response.text
        )

        # ------------------------------------------
        # 6. RETRIEVAL INSPECTOR
        # ------------------------------------------

        st.divider()

        st.subheader(
            "Retrieved Context"
        )

        st.caption(
            "These are the Top-K chunks used to "
            "generate the answer."
        )

        for index, document in enumerate(
            documents
        ):

            metadata = metadatas[index]
            distance = distances[index]

            source = metadata.get(
                "source",
                "Unknown"
            )

            page = metadata.get(
                "page"
            )

            if page:

                location = (
                    f"{source} · Page {page}"
                )

            else:

                location = source

            with st.container(
                border=True
            ):

                col1, col2 = st.columns(
                    [5, 1]
                )

                with col1:

                    st.markdown(
                        f"**{index + 1}. "
                        f"{location}**"
                    )

                with col2:

                    st.caption(
                        f"Distance: "
                        f"{distance:.4f}"
                    )

                st.write(
                    document
                )