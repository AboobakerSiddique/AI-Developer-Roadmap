from pathlib import Path

import pymupdf
from docx import Document


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".docx",
    ".md",
}


def load_txt(path: Path):
    return [{
        "content": path.read_text(encoding="utf-8"),
        "source": path.name,
        "metadata": {
            "file_type": "txt",
        },
    }]


def load_md(path: Path):
    return [{
        "content": path.read_text(encoding="utf-8"),
        "source": path.name,
        "metadata": {
            "file_type": "md",
        },
    }]


def load_pdf(path: Path):
    pdf = pymupdf.open(path)

    pages = []

    for page_number, page in enumerate(pdf, start=1):

        text = page.get_text()

        pages.append({
            "content": text,
            "source": path.name,
            "metadata": {
                "file_type": "pdf",
                "page": page_number,
            },
        })

    pdf.close()

    return pages


def load_docx(path: Path):
    document = Document(path)

    text = "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )

    return [{
        "content": text,
        "source": path.name,
        "metadata": {
            "file_type": "docx",
        },
    }]


def load_document(file_path: str):
    path = Path(file_path)

    extension = path.suffix.lower()

    if extension == ".txt":
        return load_txt(path)

    elif extension == ".md":
        return load_md(path)

    elif extension == ".pdf":
        return load_pdf(path)

    elif extension == ".docx":
        return load_docx(path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )


def load_documents(directory: str):
    directory_path = Path(directory)

    if not directory_path.exists():
        raise FileNotFoundError(
            f"Directory not found: {directory}"
        )

    documents = []

    for file_path in directory_path.rglob("*"):

        if not file_path.is_file():
            continue

        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        try:
            loaded_documents = load_document(
                str(file_path)
            )

            documents.extend(loaded_documents)

        except Exception as error:
            print(
                f"Failed to load {file_path.name}: {error}"
            )

    return documents


if __name__ == "__main__":

    documents = load_documents("documents")

    print(
        f"\nLoaded {len(documents)} document units."
    )

    for index, document in enumerate(
        documents,
        start=1
    ):

        print("\n" + "=" * 60)

        print(f"DOCUMENT UNIT: {index}")

        print(
            "SOURCE:",
            document["source"]
        )

        print(
            "METADATA:",
            document["metadata"]
        )

        print("\nCONTENT:")

        print(
            document["content"][:300]
        )