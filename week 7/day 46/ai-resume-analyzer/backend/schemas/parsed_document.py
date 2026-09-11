from pydantic import BaseModel, Field


class ParsedDocument(BaseModel):
    filename: str = Field(
        description="Original name of the uploaded PDF file"
    )

    document_type: str = Field(
        description="Type of document: 'resume' or 'job_description'"
    )

    text: str = Field(
        description="Selectable text extracted from the PDF"
    )

    page_count: int = Field(
        ge=0,
        description="Number of pages found in the PDF"
    )
