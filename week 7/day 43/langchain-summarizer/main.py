import os
import time
from google import genai
from google.genai.errors import ServerError
from dotenv import load_dotenv


load_dotenv()

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

text = input("Enter text to summarize:\n")

prompt = f"""
Summarize the following text in 3 concise sentences.



Text:
{text}
"""

# Retry logic for temporary 503 errors
max_retries = 3
for attempt in range(max_retries):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )
        print("Summary:")
        print(response.text)
        break
    except ServerError as e:
        if e.code == 503 and attempt < max_retries - 1:
            print(f"Model busy (503). Retrying in {(attempt + 1) * 2} seconds...")
            time.sleep((attempt + 1) * 2)
        else:
            raise e