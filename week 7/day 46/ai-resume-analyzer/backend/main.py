import os
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi import HTTPException
from schemas.resume_analysis import ResumeAnalysis
from services.pdf_extractor import extract_pdf


load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.environ["GEMINI_API_KEY"],
)

structured_model = model.with_structured_output(
    ResumeAnalysis
)


app = FastAPI(
    title="AI Resume Analyzer API"
)
_default_origins = "http://localhost:3000,http://127.0.0.1:3000"
allowed_origins = [
    origin.strip()
    for origin in os.environ.get("ALLOWED_ORIGINS", _default_origins).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResumeRequest(BaseModel):
    resume: str
    job_description: str


def analyze_resume(
    resume: str,
    job_description: str,
) -> ResumeAnalysis:

    prompt = f"""
    Act as a strict resume analyzer. You will be given a candidate's resume and a job description. Your task is to analyze the resume against the job description and provide a structured response in the form of a ResumeAnalysis object.
    Analyze the candidate's resume against the job description.

    Rules:
    - Only use information present in the resume.
    - Compare the resume against the job requirements.
    - Identify relevant matched and missing skills.
    - Give a realistic match score from 0 to 100.
    - Do not invent experience, skills, or qualifications.
    - Keep the recommendation concise.

    Requirement match breakdown:
    - Identify every meaningful requirement or qualification stated or clearly implied
      in the job description (skills, tools, years of experience, domain knowledge,
      certifications, etc.).
    - For each one, add an entry to requirement_match_breakdown classifying it as
      "strong_match" (clearly and directly satisfied), "partial" (related experience
      exists but does not fully meet the requirement), or "missing" (no relevant
      evidence in the resume).
    - For each entry, include short evidence quoted or paraphrased from the resume
      when it exists, or null when there is none.
    - For each entry, include a brief gap/recommended action when relevant, or null
      when status is "strong_match" with no meaningful gap.
    - Never fabricate qualifications, skills, certifications, companies, or evidence
      that are not actually present in the resume.

    RESUME:
    {resume}

    JOB DESCRIPTION:
    {job_description}
    """
    try:
        result = structured_model.invoke(prompt)

        if not isinstance(result, ResumeAnalysis):
            raise ValueError("Invalid structured output received")

        print("[INFO] Resume analysis completed successfully")

        return result

    except Exception as e:
        print(f"[ERROR] Gemini analysis failed: {e}")
        raise


@app.post(
    "/analyze",
    response_model=ResumeAnalysis,
)
def analyze(request: ResumeRequest):

    try:
        result = analyze_resume(
            request.resume,
            request.job_description,
        )

        return result

    except Exception as e:
        print(f"[ERROR] Resume analysis failed: {e}")

        raise HTTPException(
            status_code=500,
            detail="Resume analysis failed. Please try again.",
        )


def _require_pdf(upload: UploadFile, document_type: str) -> None:
    name = (upload.filename or "").lower()
    is_pdf = upload.content_type == "application/pdf" or name.endswith(".pdf")

    if not is_pdf:
        label = document_type.replace("_", " ")
        print(f"[ERROR] Rejected non-PDF upload for {document_type}")
        raise HTTPException(
            status_code=400,
            detail=f"The {label} file must be a PDF.",
        )


MIN_TEXT_CHARS = 20


async def _resolve_document(
    file: Optional[UploadFile],
    text: Optional[str],
    document_type: str,
) -> str:
    """Resolve a document's text from either an uploaded PDF or pasted text.

    Exactly one input is expected per document; the file takes precedence
    if both happen to be present. Reuses the existing PDF extraction and
    validation logic.
    """
    label = document_type.replace("_", " ")
    has_file = file is not None and bool((file.filename or "").strip())
    has_text = text is not None and bool(text.strip())

    if has_file:
        assert file is not None
        _require_pdf(file, document_type)
        content = await file.read()
        doc = extract_pdf(
            file.filename or f"{document_type}.pdf",
            document_type,
            content,
        )
        return doc.text

    if has_text:
        assert text is not None
        stripped = text.strip()
        if len(stripped) < MIN_TEXT_CHARS:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"The {label} text must be at least "
                    f"{MIN_TEXT_CHARS} characters."
                ),
            )
        return stripped

    raise HTTPException(
        status_code=400,
        detail=f"Please provide the {label} as a PDF file or pasted text.",
    )


@app.post(
    "/analyze-mixed",
    response_model=ResumeAnalysis,
)
async def analyze_mixed(
    resume: Optional[UploadFile] = File(None),
    resume_text: Optional[str] = Form(None),
    job_description: Optional[UploadFile] = File(None),
    job_description_text: Optional[str] = Form(None),
):
    resume_content = await _resolve_document(resume, resume_text, "resume")
    job_content = await _resolve_document(
        job_description, job_description_text, "job_description"
    )

    try:
        result = analyze_resume(resume_content, job_content)

        print("[INFO] Mixed analysis completed successfully")

        return result

    except Exception as e:
        print(f"[ERROR] Mixed resume analysis failed: {e}")

        raise HTTPException(
            status_code=500,
            detail="Resume analysis failed. Please try again.",
        )
