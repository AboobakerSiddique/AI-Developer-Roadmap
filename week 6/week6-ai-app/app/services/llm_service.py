from app.llm.client import generate
from app.prompts.chat_prompts import SYSTEM_PROMPT


def generate_response(message: str) -> str:

    prompt = f"""
{SYSTEM_PROMPT}

User:
{message}
"""

    try:
        return generate(prompt)

    except Exception as exc:
        print(f"[LLM ERROR] {type(exc).__name__}: {exc}")

        raise RuntimeError(
            "AI service is temporarily unavailable."
        )