"""
utils.py
Shared utility functions: logging setup, date helpers, and path resolution.
"""

import logging
from datetime import datetime
from pathlib import Path

# Base directory of the project (parent of the "modules" folder)
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"

DB_PATH = DATA_DIR / "finance.db"
JSON_EXPORT_PATH = DATA_DIR / "transactions.json"
CSV_EXPORT_PATH = DATA_DIR / "transactions.csv"
LOG_PATH = LOGS_DIR / "app.log"


def ensure_directories() -> None:
    """Create the data/ and logs/ directories if they do not already exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)


def setup_logger(name: str = "finance_manager") -> logging.Logger:
    """
    Configure and return the application logger.

    Logs are written to logs/app.log with timestamps, log level, and message.
    A logger is only configured once, even if this function is called
    multiple times (e.g. from different modules).
    """
    ensure_directories()
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.propagate = False

    return logger


def today_str() -> str:
    """Return today's date formatted as YYYY-MM-DD."""
    return datetime.now().strftime("%Y-%m-%d")


def format_currency(amount: float) -> str:
    """Format a numeric amount as a currency string, e.g. 1234.5 -> '$1,234.50'."""
    return f"${amount:,.2f}"


def is_valid_date(date_str: str) -> bool:
    """Return True if date_str matches the YYYY-MM-DD format and is a real date."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False
