import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is a Python decorator?",
    config={
    "system_instruction": "You are a strict Python interviewer. Do not give the answer directly. Give only hints.explain in 4 lines."
}
    
)

print(response.text)