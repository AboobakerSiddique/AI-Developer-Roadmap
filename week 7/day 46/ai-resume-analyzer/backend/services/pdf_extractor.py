from io import BytesIO

from fastapi import HTTPException
from pypdf import PdfReader

from schemas.parsed_document import ParsedDocument

MIN_USABLE_CHARS = 20


def extract_pdf(
    filename: str,
    document_type: str,
    content: bytes,
) -> ParsedDocument:
    """Extract selectable text from a PDF using pypdf.

    Raises HTTP 400 when the file cannot be read or contains no usable text
    (for example a scanned / image-only PDF).
    """

    label = document_type.replace("_", " ")

    print(f"[INFO] PDF received: {document_type} '{filename}' ({len(content)} bytes)")

    if not content:
        raise HTTPException(
            status_code=400,
            detail=f"The {label} file is empty. Please upload a valid PDF.",
        )

    try:
        reader = PdfReader(BytesIO(content))
        pages = reader.pages
        page_count = len(pages)
        text = "\n".join((page.extract_text() or "") for page in pages).strip()
    except Exception as e:
        print(f"[ERROR] PDF extraction failed for {document_type}: {type(e).__name__}")
        raise HTTPException(
            status_code=400,
            detail=(
                f"We could not read the {label} PDF. "
                "Please make sure it is a valid, unprotected PDF file."
            ),
        )

    if len(text) < MIN_USABLE_CHARS:
        print(
            f"[ERROR] No usable text extracted for {document_type} "
            f"(pages={page_count})"
        )
        raise HTTPException(
            status_code=400,
            detail=(
                f"No readable text was found in the {label} PDF. "
                "It looks like a scanned or image-only document. "
                "Please upload a PDF with selectable text, or paste the text instead."
            ),
        )

    print(
        f"[INFO] Extraction success: {document_type} pages={page_count} "
        f"chars={len(text)}"
    )

    return ParsedDocument(
        filename=filename,
        document_type=document_type,
        text=text,
        page_count=page_count,
    )
