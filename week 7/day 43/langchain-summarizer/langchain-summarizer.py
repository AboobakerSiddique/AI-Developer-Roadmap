import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.environ["GEMINI_API_KEY"]
)

prompt = ChatPromptTemplate.from_template(
    """
    Summarize the following text in 3 concise sentences.

    Text:
    {text}
    """
)

chain = prompt | model

text = input("Enter text to summarize:\n")

response = chain.invoke({"text": text})

print("\nSummary:")
print(response.text())