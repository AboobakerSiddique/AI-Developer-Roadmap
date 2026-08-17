import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types


# -----------------------------
# Configuration
# -----------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Add it to your .env file."
    )

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.5-flash"

MAX_RETRIES = 3


# -----------------------------
# Conversation history
# -----------------------------

conversation = []


# -----------------------------
# Ask Gemini
# -----------------------------

def ask_gemini(user_input):

    conversation.append(
        types.Content(
            role="user",
            parts=[
                types.Part(text=user_input)
            ]
        )
    )

    for attempt in range(MAX_RETRIES):

        try:

            response = client.models.generate_content(
                model=MODEL,
                contents=conversation
            )

            response_text = response.text

            if not response_text:
                raise ValueError(
                    "The model returned an empty response."
                )

            conversation.append(
                types.Content(
                    role="model",
                    parts=[
                        types.Part(text=response_text)
                    ]
                )
            )

            return response_text

        except Exception as error:

            error_message = str(error)

            print(
                f"\nAPI error: {error_message}"
            )

            # Rate limit / quota
            if "429" in error_message:

                if attempt == MAX_RETRIES - 1:
                    return (
                        "Rate limit/quota exceeded. "
                        "Please try again later."
                    )

                wait_time = 2 ** attempt

                print(
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

            # Authentication
            elif "401" in error_message:

                return (
                    "Authentication failed. "
                    "Check your GEMINI_API_KEY."
                )

            # Model/resource not found
            elif "404" in error_message:

                return (
                    "The requested model/resource "
                    "was not found."
                )

            else:

                return (
                    "An unexpected API error occurred."
                )

    return "Request failed."


# -----------------------------
# CLI
# -----------------------------

def main():

    print("=" * 50)
    print("           AI CLI ASSISTANT")
    print("=" * 50)

    print("\nType 'exit' to quit.")
    print("Type 'clear' to clear conversation history.\n")

    while True:

        user_input = input("You: ").strip()

        # Empty input
        if not user_input:
            print("Please enter a message.\n")
            continue

        # Exit
        if user_input.lower() == "exit":
            print("\nGoodbye!")
            break

        # Clear conversation
        if user_input.lower() == "clear":

            conversation.clear()

            print(
                "\nConversation history cleared.\n"
            )

            continue

        # Send to Gemini
        response = ask_gemini(user_input)

        print(f"\nAI: {response}\n")


# -----------------------------
# Entry point
# -----------------------------

if __name__ == "__main__":
    main()

import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types


# -----------------------------
# Configuration
# -----------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Add it to your .env file."
    )

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.5-flash"

MAX_RETRIES = 3


# -----------------------------
# Conversation history
# -----------------------------

conversation = []


# -----------------------------
# Ask Gemini
# -----------------------------

def ask_gemini(user_input):

    conversation.append(
        types.Content(
            role="user",
            parts=[
                types.Part(text=user_input)
            ]
        )
    )

    for attempt in range(MAX_RETRIES):

        try:

            response = client.models.generate_content(
                model=MODEL,
                contents=conversation
            )

            response_text = response.text

            if not response_text:
                raise ValueError(
                    "The model returned an empty response."
                )

            conversation.append(
                types.Content(
                    role="model",
                    parts=[
                        types.Part(text=response_text)
                    ]
                )
            )

            return response_text

        except Exception as error:

            error_message = str(error)

            print(
                f"\nAPI error: {error_message}"
            )

            # Rate limit / quota
            if "429" in error_message:

                if attempt == MAX_RETRIES - 1:
                    return (
                        "Rate limit/quota exceeded. "
                        "Please try again later."
                    )

                wait_time = 2 ** attempt

                print(
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

            # Authentication
            elif "401" in error_message:

                return (
                    "Authentication failed. "
                    "Check your GEMINI_API_KEY."
                )

            # Model/resource not found
            elif "404" in error_message:

                return (
                    "The requested model/resource "
                    "was not found."
                )

            else:

                return (
                    "An unexpected API error occurred."
                )

    return "Request failed."


# -----------------------------
# CLI
# -----------------------------

def main():

    print("=" * 50)
    print("           AI CLI ASSISTANT")
    print("=" * 50)

    print("\nType 'exit' to quit.")
    print("Type 'clear' to clear conversation history.\n")

    while True:

        user_input = input("You: ").strip()

        # Empty input
        if not user_input:
            print("Please enter a message.\n")
            continue

        # Exit
        if user_input.lower() == "exit":
            print("\nGoodbye!")
            break

        # Clear conversation
        if user_input.lower() == "clear":

            conversation.clear()

            print(
                "\nConversation history cleared.\n"
            )

            continue

        # Send to Gemini
        response = ask_gemini(user_input)

        print(f"\nAI: {response}\n")


# -----------------------------
# Entry point
# -----------------------------

if __name__ == "__main__":
    main()