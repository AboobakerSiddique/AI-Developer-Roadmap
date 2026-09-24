
import os
from dotenv import load_dotenv

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)

from langchain_chroma import Chroma

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()  # Load environment variables from .env file
# --------------------------------------------------
# CONFIG
# --------------------------------------------------

CHROMA_PATH = "./chroma_db_langchain"
COLLECTION_NAME = "langchain_documents"


# --------------------------------------------------
# EMBEDDINGS
# --------------------------------------------------

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.environ["GEMINI_API_KEY"]
)


# --------------------------------------------------
# LLM
# --------------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,
    google_api_key=os.environ["GEMINI_API_KEY"]
)


# --------------------------------------------------
# LOAD DOCUMENT
# --------------------------------------------------

def load_as_langchain_documents(file_path):

    from loader import load_document

    documents = load_document(file_path)

    langchain_documents = []

    for document in documents:

        langchain_documents.append(
            Document(
                page_content=document["content"],
                metadata={
                    "source": document["source"],
                    **document["metadata"]
                }
            )
        )

    return langchain_documents


# --------------------------------------------------
# SPLIT DOCUMENT
# --------------------------------------------------

def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)


# --------------------------------------------------
# RESET VECTOR STORE
# --------------------------------------------------

def reset_vectorstore():

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_PATH
    )

    existing_ids = vectorstore.get(
        include=[]
    )["ids"]

    if existing_ids:
        vectorstore.delete(
            ids=existing_ids
        )


# --------------------------------------------------
# CREATE VECTOR STORE
# --------------------------------------------------

def create_vectorstore(documents):

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_PATH
    )

    vectorstore.add_documents(
        documents
    )

    return vectorstore


# --------------------------------------------------
# RETRIEVER
# --------------------------------------------------

def create_retriever(vectorstore):

    return vectorstore.as_retriever(
        search_kwargs={
            "k": 3
        }
    )


# --------------------------------------------------
# FORMAT DOCUMENTS
# --------------------------------------------------

def format_documents(documents):

    return "\n\n---\n\n".join(
        document.page_content
        for document in documents
    )


# --------------------------------------------------
# RAG CHAIN
# --------------------------------------------------

def create_rag_chain(retriever):

    prompt = ChatPromptTemplate.from_template(
        """
You are a document question-answering assistant.

Answer the user's question using ONLY the
provided document context.

If the answer cannot be found in the context,
say:

"I couldn't find that information in the document."

Do not invent information.

Context:
{context}

Question:
{question}
"""
    )

    rag_chain = (
        {
            "context": retriever | format_documents,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain