"""
database.py
Handles all direct SQLite interactions: connection management, schema
creation, and CRUD operations on the transactions table.
"""

import sqlite3
from contextlib import contextmanager
from typing import Any, Dict, Generator, List, Optional

from modules.utils import DB_PATH, ensure_directories, setup_logger

logger = setup_logger()


@contextmanager
def get_connection() -> Generator[sqlite3.Connection, None, None]:
    """
    Context manager that yields a SQLite connection with row factory set
    to sqlite3.Row, and guarantees the connection is closed afterward.
    """
    ensure_directories()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except sqlite3.Error:
        conn.rollback()
        raise
    finally:
        conn.close()


def initialize_database() -> None:
    """Create the transactions table if it does not already exist."""
    try:
        with get_connection() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT NOT NULL,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT,
                    date TEXT NOT NULL
                )
                """
            )
        logger.info("Database initialized successfully.")
    except sqlite3.Error as exc:
        logger.error(f"Failed to initialize database: {exc}")
        raise


def add_transaction(tx_type: str, amount: float, category: str, description: str, date: str) -> int:
    """Insert a new transaction and return its generated ID."""
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO transactions (type, amount, category, description, date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (tx_type, amount, category, description, date),
        )
        return cursor.lastrowid


def get_all_transactions() -> List[Dict[str, Any]]:
    """Return every transaction, sorted with the newest date first."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM transactions ORDER BY date DESC, id DESC"
        ).fetchall()
        return [dict(row) for row in rows]


def get_transaction_by_id(tx_id: int) -> Optional[Dict[str, Any]]:
    """Return a single transaction by ID, or None if it does not exist."""
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM transactions WHERE id = ?", (tx_id,)
        ).fetchone()
        return dict(row) if row else None


def search_transactions(keyword: str) -> List[Dict[str, Any]]:
    """
    Search transactions where category, description, or type contains the
    given keyword (case-insensitive, partial match).
    """
    pattern = f"%{keyword.lower()}%"
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT * FROM transactions
            WHERE LOWER(category) LIKE ?
               OR LOWER(description) LIKE ?
               OR LOWER(type) LIKE ?
            ORDER BY date DESC, id DESC
            """,
            (pattern, pattern, pattern),
        ).fetchall()
        return [dict(row) for row in rows]


def update_transaction(tx_id: int, fields: Dict[str, Any]) -> bool:
    """
    Update only the provided fields for a given transaction ID.

    `fields` should be a dict whose keys are a subset of
    {"type", "amount", "category", "description"}. Returns True if a row
    was updated, False if no such transaction exists.
    """
    if not fields:
        return False

    allowed_fields = {"type", "amount", "category", "description"}
    updates = {k: v for k, v in fields.items() if k in allowed_fields}

    if not updates:
        return False

    set_clause = ", ".join(f"{col} = ?" for col in updates)
    values = list(updates.values()) + [tx_id]

    with get_connection() as conn:
        cursor = conn.execute(
            f"UPDATE transactions SET {set_clause} WHERE id = ?", values
        )
        return cursor.rowcount > 0


def delete_transaction(tx_id: int) -> bool:
    """Delete a transaction by ID. Returns True if a row was deleted."""
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM transactions WHERE id = ?", (tx_id,))
        return cursor.rowcount > 0
