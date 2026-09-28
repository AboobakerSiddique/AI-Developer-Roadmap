import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools import search, calculator


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
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


def run_agent(user_input: str):

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

    return result


if __name__ == "__main__":

    user_input = input("Ask the agent: ")

    result = run_agent(user_input)

    print("\nFINAL ANSWER")
    print("=" * 50)

    print(result["messages"][-1].content)

    print("\nAGENT ACTIVITY")
    print("=" * 50)

    for message in result["messages"]:

        print(f"\n{type(message).__name__}")

        if hasattr(message, "content"):
            print(message.content)