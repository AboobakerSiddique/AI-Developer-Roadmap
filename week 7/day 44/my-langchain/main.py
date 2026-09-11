import os
import requests
from dotenv import load_dotenv

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

# The decorator must be @tool (singular), and a docstring is mandatory so the LLM knows when to use it
@tool
def get_weather(city: str) -> str:
    """Fetch current weather details for a given city."""
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    if response.status_code != 200:
        return f"Could not retrieve weather for {city}."
    return str(response.json())

# Initialize the Gemini model (requires GOOGLE_API_KEY in your .env file)
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.7
)

system_prompt = (
    "You are a helpful assistant that can provide weather information for cities around the world, "
    "with a humorous and witty tone. Use the get_weather tool to fetch real-time weather."
)

# Create the agent via langgraph
agent = create_react_agent(
    model=llm,
    tools=[get_weather],
    prompt=system_prompt
)

# Run the query
response = agent.invoke({
    "messages": [
        {"role": "user", "content": "What is the weather like in Trivandrum?"}
    ]
})

print(response["messages"][-1].content)