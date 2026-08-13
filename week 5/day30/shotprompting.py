import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="""
Classify as:
positive
negative
neutral



classify:

Review:
"The phone looks great, but the battery dies very quickly."
"i love the design and the idea of the app, but the performance is just okay."

Return only the category.
"""
)

print(response.text)