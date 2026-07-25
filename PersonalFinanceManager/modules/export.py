"""
export.py
Handles exporting all transaction data to JSON and CSV files.
"""

import csv
import json
from typing import Tuple

from modules import database
from modules.utils import CSV_EXPORT_PATH, JSON_EXPORT_PATH, ensure_directories, setup_logger

logger = setup_logger()

CSV_FIELDNAMES = ["id", "type", "amount", "category", "description", "date"]


def export_to_json() -> Tuple[bool, str]:
    """
    Export all transactions to data/transactions.json, pretty-printed.

    Returns (success, message).
    """
    ensure_directories()
    try:
        transactions = database.get_all_transactions()
        with open(JSON_EXPORT_PATH, "w", encoding="utf-8") as f:
            json.dump(transactions, f, indent=4, ensure_ascii=False)
        logger.info(f"Exported {len(transactions)} transactions to JSON.")
        return True, f"Exported {len(transactions)} transactions to {JSON_EXPORT_PATH}"
    except (OSError, TypeError, ValueError) as exc:
        logger.error(f"JSON export failed: {exc}")
        return False, f"Failed to export JSON: {exc}"


def export_to_csv() -> Tuple[bool, str]:
    """
    Export all transactions to data/transactions.csv, including headers.

    Returns (success, message).
    """
    ensure_directories()
    try:
        transactions = database.get_all_transactions()
        with open(CSV_EXPORT_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDNAMES)
            writer.writeheader()
            for row in transactions:
                writer.writerow(row)
        logger.info(f"Exported {len(transactions)} transactions to CSV.")
        return True, f"Exported {len(transactions)} transactions to {CSV_EXPORT_PATH}"
    except (OSError, csv.Error) as exc:
        logger.error(f"CSV export failed: {exc}")
        return False, f"Failed to export CSV: {exc}"
