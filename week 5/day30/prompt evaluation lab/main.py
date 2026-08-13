from google import genai
from dotenv import load_dotenv
import os
from prompts import PROMPT_V3
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

test_cases = [
    "I was charged twice.",
    "The application crashes.",
    "I forgot my password.",
    "What time does support close?",
]

for message in test_cases:
    prompt = PROMPT_V3.format(message=message)

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
    )

    print("INPUT:", message)
    print("OUTPUT:", response.text)
    print("-" * 50)