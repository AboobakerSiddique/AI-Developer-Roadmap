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

Examples:

Review:
"The app is fantastic and very user-friendly!"
Category: positive

Review:
"The application crashes whenever I upload a PDF."
Category: negative

Review:
"I cannot change the email associated with my account."
Category: negative

Review:
"This app is okay, but it could use some improvements."
Category: neutral


Now classify:

Review:
"The phone looks great, but the battery dies very quickly."
"i love the design and the idea of the app, but the performance is just okay."

Return only the category.
"""
)

print(response.text)