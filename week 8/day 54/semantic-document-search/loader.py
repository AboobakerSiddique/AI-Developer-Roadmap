from pathlib import Path
import pymupdf
from docx import Document

SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".docx", ".md"}


def load_txt(path: Path):
    return [{
        "content": path.read_text(encoding="utf-8"),
        "source": path.name,
        "metadata": {
            "file_type": "txt"
        }
    }]


def load_md(path: Path):
    return [{
        "content": path.read_text(encoding="utf-8"),
        "source": path.name,
        "metadata": {
            "file_type": "md"
        }
    }]


def load_pdf(path: Path):
    pdf = pymupdf.open(path)

    pages = []

    for page_number, page in enumerate(pdf, start=1):
        pages.append({
            "content": page.get_text(),
            "source": path.name,
            "metadata": {
                "file_type": "pdf",
                "page": page_number
            }
        })

    pdf.close()

    return pages


def load_docx(path: Path):
    document = Document(path)

    text = "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    )

    return [{
        "content": text,
        "source": path.name,
        "metadata": {
            "file_type": "docx"
        }
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