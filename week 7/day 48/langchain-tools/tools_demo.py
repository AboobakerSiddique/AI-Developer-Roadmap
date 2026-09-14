import os
from dotenv import load_dotenv

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


@tool
def calculate(a: float, b: float, operation: str) -> float:
    """Perform basic arithmetic: add, subtract, multiply, or divide."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    raise ValueError("Unsupported operation")


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    
    # Fake data for learning
    weather = {
        "trivandrum": "30°C, partly cloudy",
        "kochi": "29°C, rainy",
        "bangalore": "24°C, cloudy",
    }

    return weather.get(
        city.lower(),
        f"No weather data available for {city}"
    )


@tool
def search_resume_skill(skill: str) -> str:
    """Check whether a skill exists in a resume database."""

    skills = {
        "python": True,
        "fastapi": True,
        "sqlalchemy": True,
        "langchain": True,
        "react": False,
        "docker": False,
    }

    exists = skills.get(skill.lower(), False)

    if exists:
        return f"{skill} is present in the resume."
    
    return f"{skill} is not present in the resume."


tools = [
    calculate,
    get_weather,
    search_resume_skill,
]

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,
)

model_with_tools = model.bind_tools(tools)


questions = [
    "What is 125 multiplied by 47?",
    "What is the weather in Trivandrum?",
    "Does the resume contain FastAPI?",
]


for question in questions:

    response = model_with_tools.invoke(question)

    print("\nUSER:")
    print(question)

    print("\nMODEL TOOL CALLS:")
    print(response.tool_calls)