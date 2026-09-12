from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
)


def load_document(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() == ".pdf":
        loader = PyPDFLoader(str(path))

    elif path.suffix.lower() == ".docx":
        loader = Docx2txtLoader(str(path))

    else:
        raise ValueError("Only PDF and DOCX files are supported.")

    documents = loader.load()

    text = "\n\n".join(
        document.page_content
        for document in documents
    )

    return text