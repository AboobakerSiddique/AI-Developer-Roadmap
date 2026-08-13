
from google import genai
from dotenv import load_dotenv
import os
import json

from prompts import EMAIL_PROMPT
from test_cases import TEST_CASES


# -----------------------------
# Configuration
# -----------------------------

load_dotenv()

# Read API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("ERROR: GEMINI_API_KEY not found in .env")
    exit()

# Initialize client
client = genai.Client(api_key=api_key)

MODEL = "gemini-3.1-flash-lite"

ALLOWED_TONES = [
    "formal",
    "friendly",
    "concise",
    "apologetic",
]


# -----------------------------
# Generate Email
# -----------------------------

def generate_email(purpose, recipient, tone, key_points):

    prompt = EMAIL_PROMPT.format(
        purpose=purpose,
        recipient=recipient,
        tone=tone,
        key_points="\n".join(
            f"- {point}" for point in key_points
        ),
    )

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": {
                    "type": "OBJECT",
                    "properties": {
                        "subject": {
                            "type": "STRING"
                        },
                        "body": {
                            "type": "STRING"
                        },
                    },
                    "required": [
                        "subject",
                        "body",
                    ],
                },
            },
        )

        try:
            email = json.loads(response.text)

        except json.JSONDecodeError:
            print("ERROR: Gemini returned invalid JSON.")
            return None

        if "subject" not in email or "body" not in email:
            print("ERROR: Response is missing subject or body.")
            return None

        return email

    except Exception as e:

        error_message = str(e)

        if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
            print("ERROR: Gemini API quota exceeded.")
            print("Wait for the quota to reset.")

        elif "401" in error_message or "API key" in error_message:
            print("ERROR: Check your Gemini API key.")

        else:
            print("ERROR:", e)

        return None


# -----------------------------
# Manual Mode
# -----------------------------

def manual_mode():

    print("\n=== AI EMAIL GENERATOR ===\n")

    purpose = input("Purpose: ").strip()
    recipient = input("Recipient: ").strip()
    tone = input("Tone: ").strip().lower()

    if not purpose:
        print("Purpose cannot be empty.")
        return

    if not recipient:
        print("Recipient cannot be empty.")
        return

    if tone not in ALLOWED_TONES:
        print("Invalid tone.")
        print("Choose:", ", ".join(ALLOWED_TONES))
        return

    print("\nEnter key points.")
    print("Type 'done' when finished.\n")

    key_points = []

    while True:

        point = input("- ").strip()

        if point.lower() == "done":
            break

        if point:
            key_points.append(point)

    if not key_points:
        print("At least one key point is required.")
        return

    email = generate_email(
        purpose,
        recipient,
        tone,
        key_points,
    )

    if email:

        print("\n" + "=" * 50)
        print("GENERATED EMAIL")
        print("=" * 50)

        print("\nSubject:")
        print(email["subject"])

        print("\nBody:")
        print(email["body"])


# -----------------------------
# Test Mode
# -----------------------------

def test_mode():

    print("\n=== RUNNING TEST CASES ===\n")

    total = len(TEST_CASES)
    passed = 0

    for index, test in enumerate(TEST_CASES, start=1):

        print("=" * 60)
        print(f"TEST {index}: {test['name']}")
        print("=" * 60)

        email = generate_email(
            test["purpose"],
            test["recipient"],
            test["tone"],
            test["key_points"],
        )

        if not email:
            print("❌ FAILED — No valid response")
            continue

        print("\nSubject:")
        print(email["subject"])

        print("\nBody:")
        print(email["body"])

        print("\n--- Expected Key Points ---")

        for point in test["key_points"]:
            print(f"- {point}")

        print("\n⚠️ Manual evaluation required.")

        score = input(
            "Score this test (0-4): "
        ).strip()

        try:
            score = int(score)

            if 0 <= score <= 4:

                if score == 4:
                    passed += 1

                print(f"Score: {score}/4")

            else:
                print("Invalid score.")

        except ValueError:
            print("Invalid score.")

        print()

    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    print(f"Tests: {total}")
    print(f"Perfect scores: {passed}/{total}")


# -----------------------------
# Main Menu
# -----------------------------

def main():

    while True:

        print("\n")
        print("=" * 40)
        print("AI EMAIL GENERATOR")
        print("=" * 40)

        print("1. Generate Email")
        print("2. Run Test Cases")
        print("3. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            manual_mode()

        elif choice == "2":
            test_mode()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()