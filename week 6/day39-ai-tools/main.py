from fastapi import FastAPI
from google.genai import types

from llm import client
from tools import get_user_tasks
from github_tools import get_github_repository

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Day 39 tool calling API"}


@app.post("/chat")
def chat(message: str):
    # Simulated authenticated user
    current_user_id = "user_123"

    print(f"👤 User: {message}")
    print(f"🔐 Authenticated user: {current_user_id}")

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=message,
        config=types.GenerateContentConfig(
            tools=[
                get_user_tasks,
                get_github_repository,
            ]
        ),
    )

    print(f"🤖 Gemini response: {response.text}")

    return {
        "response": response.text
    }