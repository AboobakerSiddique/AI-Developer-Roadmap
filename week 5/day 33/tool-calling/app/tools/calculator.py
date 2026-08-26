def calculator(a: float, b: float, operation: str):
    """
     Perform a mathematical operation on two numbers.

    Args:
        a: The first number.
        b: The second number.
        operation: The operation to perform.
                   Supported operations:
                   add, subtract, multiply, divide.
    """

    if operation == "add":
        return a + b

    if operation == "subtract":
        return a - b

    if operation == "multiply":
        return a * b

    if operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")

        return a / b

    raise ValueError(
        f"Unsupported operation: {operation}"
    )