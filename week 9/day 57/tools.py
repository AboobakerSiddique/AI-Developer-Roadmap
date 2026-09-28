from langchain_core.tools import tool


@tool
def search(query: str) -> str:
    """Search the available knowledge source for factual information."""

    query = query.lower().strip()

    knowledge = {
        "india population":
            "India's population is approximately 1.4 billion.",
        "japan population":
            "Japan's population is approximately 123 million.",
        "python":
            "Python is a high-level general-purpose programming language."
    }

    for key, value in knowledge.items():
        if key in query:
            return value

    return "No information found."


@tool
def calculator(expression: str) -> str:
    """Perform a mathematical calculation."""

    allowed = "0123456789+-*/(). "

    if not all(char in allowed for char in expression):
        raise ValueError("Invalid mathematical expression")

    return str(eval(expression))