from typing import Literal, Optional

from pydantic import BaseModel, Field


class RequirementMatch(BaseModel):
    requirement: str = Field(
        description="A specific, meaningful requirement or qualification taken from the job description"
    )

    status: Literal["strong_match", "partial", "missing"] = Field(
        description=(
            "How well the resume satisfies this requirement: 'strong_match' if clearly "
            "and directly satisfied, 'partial' if related experience exists but doesn't "
            "fully meet the requirement, or 'missing' if no relevant evidence is present"
        )
    )

    evidence: Optional[str] = Field(
        default=None,
        description=(
            "Specific evidence from the resume that supports this status. "
            "Must be grounded in the actual resume text. Null if status is 'missing' "
            "and nothing relevant was found."
        )
    )

    gap: Optional[str] = Field(
        default=None,
        description=(
            "A short, concrete gap description or recommended action for the candidate. "
            "Null when status is 'strong_match' and there is no meaningful gap."
        )
    )


class ResumeAnalysis(BaseModel):
    candidate_name: str = Field(
        description="The candidate's full name"
    )

    matched_skills: list[str] = Field(
        description="Skills from the job description that the candidate has"
    )

    missing_skills: list[str] = Field(
        description="Important job requirements missing from the resume"
    )

    strengths: list[str] = Field(
        description="The candidate's strongest relevant qualifications"
    )

    weaknesses: list[str] = Field(
        description="Relevant weaknesses or gaps in the candidate's profile"
    )

    match_score: int = Field(
        ge=0,
        le=100,
        description="Overall resume-to-job match score from 0 to 100"
    )

    recommendation: str = Field(
        description="Overall hiring recommendation with brief reasoning"
    )

    requirement_match_breakdown: list[RequirementMatch] = Field(
        default_factory=list,
        description=(
            "A requirement-by-requirement comparison of the resume against the job "
            "description. Include one entry for every meaningful requirement stated "
            "or clearly implied in the job description."
        )
    )
