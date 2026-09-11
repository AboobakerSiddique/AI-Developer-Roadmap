import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)

load_dotenv()  # Load environment variables from .env file

SYSTEM_PROMPT = (
    "You are a helpful AI assistant. "
    "Answer clearly and concisely."
)


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.environ["GEMINI_API_KEY"],
)


def clear_history():
    return [
        SystemMessage(content=SYSTEM_PROMPT)
    ]


history = clear_history()


print("LangChain Chat Assistant")
print("Type /clear to clear the conversation.")
print("Type /exit to quit.")


while True:
    user_input = input("\nYou: ").strip()

    if not user_input:
        continue

    if user_input.lower() == "/exit":
        print("Goodbye!")
        break

    if user_input.lower() == "/clear":
        history = clear_history()
        print("Conversation cleared.")
        continue

    history.append(
        HumanMessage(content=user_input)
    )

    try:
        response = model.invoke(history)

    except Exception as e:
        print(f"\nError: {e}")

        # Remove the failed user message
        history.pop()

        continue

    history.append(response)

    print(f"\nAI: {response.content}")