"""
reports.py
Aggregation and reporting logic, such as the monthly summary.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional

from modules import database
from modules.utils import setup_logger

logger = setup_logger()


def _empty_summary() -> Dict[str, Any]:
    """Return a summary dict with all values zeroed / None, used when no data exists."""
    return {
        "total_income": 0.0,
        "total_expense": 0.0,
        "net_savings": 0.0,
        "highest_expense": None,
        "highest_income": None,
        "average_expense": 0.0,
        "average_income": 0.0,
        "total_transactions": 0,
    }


def generate_monthly_summary(year: int, month: int) -> Dict[str, Any]:
    """
    Compute a financial summary for a specific year/month.

    Returns a dictionary with total income, total expense, net savings,
    highest/lowest transactions, averages, and transaction count.
    """
    try:
        all_transactions: List[Dict[str, Any]] = database.get_all_transactions()
    except Exception as exc:  # noqa: BLE001 - surfaced to caller via logging
        logger.error(f"Failed to fetch transactions for summary: {exc}")
        return _empty_summary()

    month_prefix = f"{year:04d}-{month:02d}"
    monthly = [t for t in all_transactions if str(t["date"]).startswith(month_prefix)]

    if not monthly:
        return _empty_summary()

    incomes = [t for t in monthly if t["type"] == "income"]
    expenses = [t for t in monthly if t["type"] == "expense"]

    total_income = sum(t["amount"] for t in incomes)
    total_expense = sum(t["amount"] for t in expenses)

    highest_income = max(incomes, key=lambda t: t["amount"], default=None)
    highest_expense = max(expenses, key=lambda t: t["amount"], default=None)

    average_income = (total_income / len(incomes)) if incomes else 0.0
    average_expense = (total_expense / len(expenses)) if expenses else 0.0

    return {
        "total_income": round(total_income, 2),
        "total_expense": round(total_expense, 2),
        "net_savings": round(total_income - total_expense, 2),
        "highest_expense": highest_expense,
        "highest_income": highest_income,
        "average_expense": round(average_expense, 2),
        "average_income": round(average_income, 2),
        "total_transactions": len(monthly),
    }


def current_month_summary() -> Dict[str, Any]:
    """Convenience wrapper that generates the summary for the current month."""
    now = datetime.now()
    return generate_monthly_summary(now.year, now.month)
