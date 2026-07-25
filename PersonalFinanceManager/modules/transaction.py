"""
transaction.py
Business logic layer that sits between the UI and the database module.
Combines validation with database operations and handles logging of
transaction-related events.
"""

import sqlite3
from typing import Any, Dict, List, Optional, Tuple

from modules import database
from modules.utils import setup_logger, today_str
from modules.validation import (
    validate_amount,
    validate_category,
    validate_description,
)

logger = setup_logger()


def create_transaction(
    tx_type: str, raw_amount: str, category: str, description: str
) -> Tuple[bool, str, Optional[int]]:
    """
    Validate and create a new income or expense transaction dated today.

    Returns (success, message, new_id).
    """
    amount_ok, amount_err, amount = validate_amount(raw_amount)
    if not amount_ok:
        return False, amount_err, None

    category_ok, category_err = validate_category(category)
    if not category_ok:
        return False, category_err, None

    description_ok, description_err = validate_description(description)
    if not description_ok:
        return False, description_err, None

    try:
        new_id = database.add_transaction(
            tx_type=tx_type,
            amount=amount,
            category=category.strip(),
            description=(description or "").strip(),
            date=today_str(),
        )
        logger.info(
            f"Added {tx_type} transaction (ID {new_id}): "
            f"{amount} in category '{category.strip()}'"
        )
        return True, f"{tx_type.capitalize()} added successfully (ID {new_id}).", new_id
    except sqlite3.Error as exc:
        logger.error(f"Database error while adding transaction: {exc}")
        return False, f"Database error: {exc}", None


def list_transactions() -> List[Dict[str, Any]]:
    """Return all transactions, newest first."""
    try:
        return database.get_all_transactions()
    except sqlite3.Error as exc:
        logger.error(f"Database error while listing transactions: {exc}")
        return []


def find_transactions(keyword: str) -> List[Dict[str, Any]]:
    """Search transactions by category, description, or type."""
    try:
        return database.search_transactions(keyword)
    except sqlite3.Error as exc:
        logger.error(f"Database error while searching transactions: {exc}")
        return []


def edit_transaction(
    tx_id: int,
    tx_type: Optional[str] = None,
    raw_amount: Optional[str] = None,
    category: Optional[str] = None,
    description: Optional[str] = None,
) -> Tuple[bool, str]:
    """
    Update only the fields that were provided (non-None / non-empty).

    Returns (success, message).
    """
    existing = database.get_transaction_by_id(tx_id)
    if not existing:
        return False, f"No transaction found with ID {tx_id}."

    updates: Dict[str, Any] = {}

    if tx_type:
        updates["type"] = tx_type.lower()

    if raw_amount:
        amount_ok, amount_err, amount = validate_amount(raw_amount)
        if not amount_ok:
            return False, amount_err
        updates["amount"] = amount

    if category:
        category_ok, category_err = validate_category(category)
        if not category_ok:
            return False, category_err
        updates["category"] = category.strip()

    if description is not None:
        description_ok, description_err = validate_description(description)
        if not description_ok:
            return False, description_err
        updates["description"] = description.strip()

    if not updates:
        return False, "No fields were provided to update."

    try:
        updated = database.update_transaction(tx_id, updates)
        if updated:
            logger.info(f"Updated transaction ID {tx_id}: {updates}")
            return True, f"Transaction {tx_id} updated successfully."
        return False, f"No transaction found with ID {tx_id}."
    except sqlite3.Error as exc:
        logger.error(f"Database error while updating transaction {tx_id}: {exc}")
        return False, f"Database error: {exc}"


def remove_transaction(tx_id: int) -> Tuple[bool, str]:
    """Delete a transaction by ID. Returns (success, message)."""
    try:
        deleted = database.delete_transaction(tx_id)
        if deleted:
            logger.info(f"Deleted transaction ID {tx_id}")
            return True, f"Transaction {tx_id} deleted successfully."
        return False, f"No transaction found with ID {tx_id}."
    except sqlite3.Error as exc:
        logger.error(f"Database error while deleting transaction {tx_id}: {exc}")
        return False, f"Database error: {exc}"


def get_transaction(tx_id: int) -> Optional[Dict[str, Any]]:
    """Fetch a single transaction by ID."""
    try:
        return database.get_transaction_by_id(tx_id)
    except sqlite3.Error as exc:
        logger.error(f"Database error while fetching transaction {tx_id}: {exc}")
        return None
