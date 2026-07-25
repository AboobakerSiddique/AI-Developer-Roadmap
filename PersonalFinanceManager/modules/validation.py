"""
validation.py
Centralized validation logic for user input. Every validator returns a
(is_valid, error_message) tuple so callers can decide how to react.
"""

from typing import Optional, Tuple

MAX_DESCRIPTION_LENGTH = 250
VALID_TYPES = ("income", "expense")


class ValidationError(Exception):
    """Raised when a validation rule is violated and the caller wants a hard stop."""


def validate_amount(raw_amount: str) -> Tuple[bool, Optional[str], Optional[float]]:
    """
    Validate a raw amount string.

    Returns (is_valid, error_message, parsed_value).
    Rejects negative amounts, zero amounts, and non-numeric input.
    """
    try:
        amount = float(raw_amount)
    except (TypeError, ValueError):
        return False, "Amount must be a valid number.", None

    if amount <= 0:
        return False, "Amount must be greater than zero.", None

    return True, None, round(amount, 2)


def validate_category(category: str) -> Tuple[bool, Optional[str]]:
    """Validate that a category is non-empty after stripping whitespace."""
    if category is None or not category.strip():
        return False, "Category cannot be empty."
    return True, None


def validate_description(description: str) -> Tuple[bool, Optional[str]]:
    """Validate that a description does not exceed the maximum allowed length."""
    if description is None:
        return True, None
    if len(description) > MAX_DESCRIPTION_LENGTH:
        return False, f"Description cannot exceed {MAX_DESCRIPTION_LENGTH} characters."
    return True, None


def validate_transaction_type(tx_type: str) -> Tuple[bool, Optional[str]]:
    """Validate that a transaction type is either 'income' or 'expense'."""
    if tx_type is None or tx_type.lower() not in VALID_TYPES:
        return False, "Type must be either 'income' or 'expense'."
    return True, None


def validate_menu_choice(raw_choice: str, valid_choices: range) -> Tuple[bool, Optional[str], Optional[int]]:
    """
    Validate a menu selection.

    Returns (is_valid, error_message, parsed_choice).
    """
    if not raw_choice or not raw_choice.strip().isdigit():
        return False, "Please enter a valid number.", None

    choice = int(raw_choice.strip())
    if choice not in valid_choices:
        return False, f"Please enter a number between {min(valid_choices)} and {max(valid_choices)}.", None

    return True, None, choice


def validate_id(raw_id: str) -> Tuple[bool, Optional[str], Optional[int]]:
    """Validate that a raw string represents a positive integer ID."""
    if not raw_id or not raw_id.strip().isdigit():
        return False, "ID must be a positive whole number.", None

    tx_id = int(raw_id.strip())
    if tx_id <= 0:
        return False, "ID must be a positive whole number.", None

    return True, None, tx_id
