from google import genai

from app.config import settings


if not settings.GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is not configured"
    )


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def generate(message: str) -> str:

    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=message,
    )

    if not response.text:
        raise RuntimeError(
            "Gemini returned an empty response"
        )

    return response.text