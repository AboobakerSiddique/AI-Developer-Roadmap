import os

from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

@tool
def calculator(expression: str) -> str:
    """Perform a mathematical calculation."""
    
    allowed = "0123456789+-*/(). "

    if not all(char in allowed for char in expression):
        raise ValueError("Invalid mathematical expression")

    return str(eval(expression))

@tool
def search(query: str) -> str:
    """Search the available knowledge source for information."""

    query = query.lower().strip()

    if "india" in query and "population" in query:
        return "India's population is approximately 1.4 billion."

    if "japan" in query and "population" in query:
        return "Japan's population is approximately 123 million."

    if "python" in query:
        return "Python is a high-level general-purpose programming language."

    return "No information found."

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0,
    google_api_key=os.environ["GEMINI_API_KEY"]
)

tools = [
    search,
    calculator
]
agent = create_agent(
    model=llm,
    tools=tools
)
user_input = input("Ask the agent: ")

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    }
)

print("\nFinal answer:")

print(
    result["messages"][-1].content
)