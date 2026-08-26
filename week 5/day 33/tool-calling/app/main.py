import logging
import os

from dotenv import load_dotenv
from google import genai

from app.tools.calculator import calculator
from app.tools.weather import get_weather
from app.tools.time import get_time


# ==================================================
# Configuration
# ==================================================

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing from .env"
    )


MODEL_NAME = "gemini-3.5-flash"


# ==================================================
# Gemini Client
# ==================================================

client = genai.Client(
    api_key=API_KEY
)


# ==================================================
# Tool Registry
# ==================================================

AVAILABLE_TOOLS = {
    "calculator": calculator,
    "get_weather": get_weather,
    "get_time": get_time
}


TOOLS = [
    calculator,
    get_weather,
    get_time
]


# ==================================================
# Execute Tool
# ==================================================

def execute_tool(function_call):
    """
    Execute a tool requested by Gemini.
    """

    tool_name = function_call.name
    arguments = function_call.args or {}

    logger.info(
        "Tool requested: %s",
        tool_name
    )

    logger.info(
        "Tool arguments: %s",
        arguments
    )

    # ----------------------------------------------
    # Check whether tool exists
    # ----------------------------------------------

    if tool_name not in AVAILABLE_TOOLS:

        raise ValueError(
            f"Unknown tool requested: {tool_name}"
        )

    tool_function = AVAILABLE_TOOLS[
        tool_name
    ]

    # ----------------------------------------------
    # Execute tool
    # ----------------------------------------------

    try:

        result = tool_function(
            **arguments
        )

    except Exception:

        logger.exception(
            "Tool execution failed."
        )

        raise

    logger.info(
        "Tool result: %s",
        result
    )

    return result


# ==================================================
# Ask Gemini
# ==================================================

def ask_gemini(
    user_prompt: str
) -> str:

    logger.info(
        "User prompt: %s",
        user_prompt
    )

    # ----------------------------------------------
    # First Gemini request
    # ----------------------------------------------

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=user_prompt,
        config={
            "tools": TOOLS
        }
    )

    # ----------------------------------------------
    # No tool required
    # ----------------------------------------------

    if not response.function_calls:

        logger.info(
            "No tool requested."
        )

        return response.text

    # ----------------------------------------------
    # Tool call
    # ----------------------------------------------

    function_call = response.function_calls[0]

    logger.info(
        "Gemini selected: %s",
        function_call.name
    )

    # ----------------------------------------------
    # Execute selected tool
    # ----------------------------------------------

    tool_result = execute_tool(
        function_call
    )

    # ----------------------------------------------
    # Send result back to Gemini
    # ----------------------------------------------

    follow_up = client.models.generate_content(
        model=MODEL_NAME,
        contents=[
            response.candidates[0].content,
            {
                "role": "user",
                "parts": [
                    {
                        "function_response": {
                            "name": function_call.name,
                            "response": {
                                "result": tool_result
                            }
                        }
                    }
                ]
            }
        ],
        config={
            "tools": TOOLS
        }
    )

    return follow_up.text


# ==================================================
# CLI
# ==================================================

def main():

    print("=" * 60)
    print("Day 33 - Multi-Tool AI Assistant")
    print("=" * 60)

    print(
        "\nAvailable tools:"
    )

    print(
        "  • calculator"
    )

    print(
        "  • get_weather"
    )

    print(
        "  • get_time"
    )

    print(
        "\nType 'exit' to quit.\n"
    )

    while True:

        try:

            user_prompt = input("You: ")

        except KeyboardInterrupt:

            print(
                "\nGoodbye!"
            )

            break

        if user_prompt.strip().lower() == "exit":

            print(
                "Goodbye!"
            )

            break

        if not user_prompt.strip():

            continue

        try:

            answer = ask_gemini(
                user_prompt
            )

            print(
                f"\nAI: {answer}\n"
            )

        except Exception as error:

            logger.exception(
                "Application error"
            )

            print(
                f"\nError: {error}\n"
            )


# ==================================================
# Entry Point
# ==================================================

if __name__ == "__main__":
    main()