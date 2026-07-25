#!/usr/bin/env python3
"""
main.py
Entry point for the Personal Finance Manager CLI application.

Run with:
    python main.py
"""

import sys
from datetime import datetime

from modules import database, export, reports, transaction, ui
from modules.utils import setup_logger
from modules.validation import validate_id, validate_menu_choice

logger = setup_logger()

MENU_RANGE = range(1, 11)


def handle_add_transaction(tx_type: str) -> None:
    """Prompt for and create a new income or expense transaction."""
    console_title = "Add Income" if tx_type == "income" else "Add Expense"
    ui.console.print()
    ui.console.print(f"[bold underline]{console_title}[/bold underline]")

    raw_amount = ui.prompt_input("Amount")
    category = ui.prompt_input("Category")
    description = ui.prompt_input("Description (optional)", default="")

    success, message, _ = transaction.create_transaction(
        tx_type=tx_type,
        raw_amount=raw_amount,
        category=category,
        description=description,
    )

    if success:
        ui.print_success(message)
    else:
        ui.print_error(message)


def handle_view_transactions() -> None:
    """Fetch and display all transactions."""
    transactions = transaction.list_transactions()
    ui.render_transactions_table(transactions, title="All Transactions")


def handle_search_transactions() -> None:
    """Prompt for a keyword and display matching transactions."""
    keyword = ui.prompt_input("Enter search keyword (category, description, or type)")
    if not keyword.strip():
        ui.print_warning("Search keyword cannot be empty.")
        return

    results = transaction.find_transactions(keyword.strip())
    ui.render_transactions_table(results, title=f"Search Results for '{keyword}'")


def handle_update_transaction() -> None:
    """Prompt for a transaction ID and updated fields, then apply the update."""
    raw_id = ui.prompt_input("Enter the ID of the transaction to update")
    id_ok, id_err, tx_id = validate_id(raw_id)
    if not id_ok:
        ui.print_error(id_err)
        return

    existing = transaction.get_transaction(tx_id)
    if not existing:
        ui.print_error(f"No transaction found with ID {tx_id}.")
        return

    ui.render_transactions_table([existing], title="Current Transaction")
    ui.print_info("Leave a field blank to keep its current value.")

    new_type = ui.prompt_input("New type (income/expense)", default="")
    new_amount = ui.prompt_input("New amount", default="")
    new_category = ui.prompt_input("New category", default="")
    new_description = ui.prompt_input("New description", default="")

    success, message = transaction.edit_transaction(
        tx_id=tx_id,
        tx_type=new_type if new_type.strip() else None,
        raw_amount=new_amount if new_amount.strip() else None,
        category=new_category if new_category.strip() else None,
        description=new_description if new_description.strip() else None,
    )

    if success:
        ui.print_success(message)
    else:
        ui.print_error(message)


def handle_delete_transaction() -> None:
    """Prompt for a transaction ID and delete it after confirmation."""
    raw_id = ui.prompt_input("Enter the ID of the transaction to delete")
    id_ok, id_err, tx_id = validate_id(raw_id)
    if not id_ok:
        ui.print_error(id_err)
        return

    existing = transaction.get_transaction(tx_id)
    if not existing:
        ui.print_error(f"No transaction found with ID {tx_id}.")
        return

    ui.render_transactions_table([existing], title="Transaction to Delete")

    if not ui.confirm("Are you sure you want to delete this transaction?"):
        ui.print_info("Deletion cancelled.")
        return

    success, message = transaction.remove_transaction(tx_id)
    if success:
        ui.print_success(message)
    else:
        ui.print_error(message)


def handle_monthly_summary() -> None:
    """Prompt for a year/month (defaulting to the current month) and display the summary."""
    now = datetime.now()
    raw_year = ui.prompt_input("Year", default=str(now.year))
    raw_month = ui.prompt_input("Month (1-12)", default=str(now.month))

    try:
        year = int(raw_year)
        month = int(raw_month)
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
    except ValueError:
        ui.print_error("Please enter a valid year and month (month between 1 and 12).")
        return

    summary = reports.generate_monthly_summary(year, month)
    ui.render_monthly_summary(summary, year, month)


def handle_export_json() -> None:
    """Export all transactions to JSON."""
    success, message = export.export_to_json()
    if success:
        ui.print_success(message)
    else:
        ui.print_error(message)


def handle_export_csv() -> None:
    """Export all transactions to CSV."""
    success, message = export.export_to_csv()
    if success:
        ui.print_success(message)
    else:
        ui.print_error(message)


def dispatch(choice: int) -> bool:
    """
    Execute the action for a given validated menu choice.

    Returns False if the application should exit, True otherwise.
    """
    actions = {
        1: lambda: handle_add_transaction("income"),
        2: lambda: handle_add_transaction("expense"),
        3: handle_view_transactions,
        4: handle_search_transactions,
        5: handle_update_transaction,
        6: handle_delete_transaction,
        7: handle_monthly_summary,
        8: handle_export_json,
        9: handle_export_csv,
    }

    if choice == 10:
        return False

    action = actions.get(choice)
    if action:
        try:
            action()
        except Exception as exc:  # noqa: BLE001 - top-level safety net per feature
            logger.error(f"Unhandled error while executing menu option {choice}: {exc}")
            ui.print_error(f"An unexpected error occurred: {exc}")

    return True


def run() -> None:
    """Main application loop."""
    logger.info("Program start")
    database.initialize_database()

    ui.print_header()

    running = True
    while running:
        try:
            ui.print_main_menu()
            raw_choice = ui.prompt_input("Select an option")
            valid, error, choice = validate_menu_choice(raw_choice, MENU_RANGE)

            if not valid:
                ui.print_error(error)
                continue

            running = dispatch(choice)

        except KeyboardInterrupt:
            ui.console.print()
            ui.print_warning("Interrupted by user.")
            running = False
        except Exception as exc:  # noqa: BLE001 - guarantees the app never crashes
            logger.error(f"Unhandled exception in main loop: {exc}")
            ui.print_error(f"An unexpected error occurred: {exc}")

    ui.print_goodbye()
    logger.info("Program exit")


if __name__ == "__main__":
    try:
        run()
    except Exception as exc:  # noqa: BLE001 - absolute last resort safety net
        logger.error(f"Fatal error: {exc}")
        print(f"Fatal error: {exc}")
        sys.exit(1)
