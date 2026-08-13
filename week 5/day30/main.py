import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="""
You are a senior Python backend developer.

The developer already knows Python, FastAPI,
REST APIs, password hashing and HTTP.

Explain JWT authentication.

Do not explain basic Python.
Use technically accurate terminology.
Include one practical example.

Structure your answer as:

1. Concept
2. Authentication flow
3. Example
4. Common mistakes
"""
)

print(response.text)