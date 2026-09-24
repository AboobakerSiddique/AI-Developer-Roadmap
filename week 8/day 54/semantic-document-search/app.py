import os
import tempfile
from pathlib import Path

import streamlit as st

from langchain_rag import (
    load_as_langchain_documents,
    split_documents,
    reset_vectorstore,
    create_vectorstore,
    create_retriever,
    create_rag_chain
)


# --------------------------------------------------
# CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="LangChain RAG",
    page_icon="⌕",
    layout="wide"
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "indexed" not in st.session_state:
    st.session_state.indexed = False

if "indexed_file" not in st.session_state:
    st.session_state.indexed_file = None

if "chunk_count" not in st.session_state:
    st.session_state.chunk_count = 0

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("LangChain RAG")

st.caption(
    "Document retrieval and question answering "
    "with LangChain + Gemini + Chroma"
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
# INDEX DOCUMENT
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
                "Processing document..."
            ):

                # ------------------------------------------
                # 1. CLEAR PREVIOUS LANGCHAIN STORE
                # ------------------------------------------

                reset_vectorstore()

                # ------------------------------------------
                # 2. LOAD
                # ------------------------------------------

                documents = (
                    load_as_langchain_documents(
                        temp_path
                    )
                )

                # ------------------------------------------
                # 3. SPLIT
                # ------------------------------------------

                chunks = split_documents(
                    documents
                )

                if not chunks:
                    st.error(
                        "No readable text was found."
                    )
                    st.stop()

                # ------------------------------------------
                # 4. EMBED + STORE
                # ------------------------------------------

                vectorstore = create_vectorstore(
                    chunks
                )

                # ------------------------------------------
                # 5. CREATE RETRIEVER
                # ------------------------------------------

                retriever = create_retriever(
                    vectorstore
                )

                # ------------------------------------------
                # 6. CREATE RAG CHAIN
                # ------------------------------------------

                rag_chain = create_rag_chain(
                    retriever
                )

                # ------------------------------------------
                # SESSION STATE
                # ------------------------------------------

                st.session_state.indexed = True

                st.session_state.indexed_file = (
                    uploaded_file.name
                )

                st.session_state.chunk_count = (
                    len(chunks)
                )

                st.session_state.retriever = (
                    retriever
                )

                st.session_state.rag_chain = (
                    rag_chain
                )

            st.success(
                f"Indexed {len(chunks)} chunks."
            )

        except Exception as error:

            st.error(
                f"Indexing failed: {error}"
            )

        finally:

            try:
                os.remove(temp_path)
            except OSError:
                pass


# --------------------------------------------------
# QUESTION ANSWERING
# --------------------------------------------------

st.divider()

st.subheader("Ask your document")


if not st.session_state.indexed:

    st.info(
        "Upload and index a document first."
    )

else:

    query = st.text_input(
        "Question",
        placeholder=(
            "e.g. What is the main purpose "
            "of this document?"
        )
    )

    if query:

        # ------------------------------------------
        # RETRIEVE
        # ------------------------------------------

        with st.spinner(
            "Retrieving relevant context..."
        ):

            retrieved_docs = (
                st.session_state.retriever.invoke(
                    query
                )
            )

        # ------------------------------------------
        # GENERATE ANSWER
        # ------------------------------------------

        with st.spinner(
            "Generating answer..."
        ):

            answer = (
                st.session_state.rag_chain.invoke(
                    query
                )
            )

        # ------------------------------------------
        # ANSWER
        # ------------------------------------------

        st.subheader("Answer")

        st.write(answer)

        # ------------------------------------------
        # SOURCES
        # ------------------------------------------

        st.divider()

        st.subheader(
            "Retrieved Context"
        )

        st.caption(
            "Top-K documents retrieved by "
            "the LangChain retriever."
        )

        for index, document in enumerate(
            retrieved_docs
        ):

            source = document.metadata.get(
                "source",
                "Unknown"
            )

            page = document.metadata.get(
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

                st.markdown(
                    f"**{index + 1}. "
                    f"{location}**"
                )

                st.write(
                    document.page_content
                )