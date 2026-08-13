import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="""
    Explain REST APIs to a beginner.

    Give:
    1. Definition
    2. Real-world analogy
    3. Python example
    4. One common mistake
    """,
    config={
        "temperature": 0.2,
        "max_output_tokens": 50000,
        "system_instruction": """
        You are an experienced backend development teacher.
        The learner already knows Python and FastAPI.
        Don't explain basic Python syntax.
        """
    }
)
print(response.text)