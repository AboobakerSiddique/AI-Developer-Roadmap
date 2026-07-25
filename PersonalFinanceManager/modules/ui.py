"""
ui.py
All Rich-based presentation logic: menus, tables, panels, and prompts.
Keeping this separate means the rest of the app has no direct dependency
on how things are displayed.
"""

from typing import Any, Dict, List, Optional

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.rule import Rule
from rich.table import Table
from rich.text import Text

from modules.utils import format_currency

console = Console()

MENU_OPTIONS = {
    1: "Add Income",
    2: "Add Expense",
    3: "View Transactions",
    4: "Search Transactions",
    5: "Update Transaction",
    6: "Delete Transaction",
    7: "Monthly Summary",
    8: "Export JSON",
    9: "Export CSV",
    10: "Exit",
}


def print_header() -> None:
    """Print the application header banner."""
    console.print()
    console.print(
        Panel(
            Text("PERSONAL FINANCE MANAGER", justify="center", style="bold white"),
            style="bold blue",
            expand=True,
        )
    )


def print_main_menu() -> None:
    """Render the main menu options."""
    console.print(Rule("[bold cyan]Main Menu[/bold cyan]"))
    for key, label in MENU_OPTIONS.items():
        console.print(f"  [bold yellow]{key:>2}[/bold yellow]  {label}")
    console.print(Rule())


def prompt_input(message: str, default: Optional[str] = None) -> str:
    """Prompt the user for free-text input, optionally with a default value."""
    if default is not None:
        return Prompt.ask(f"[cyan]{message}[/cyan]", default=default)
    return Prompt.ask(f"[cyan]{message}[/cyan]", default="")


def print_success(message: str) -> None:
    """Print a success message in green."""
    console.print(f"[bold green]✔ {message}[/bold green]")


def print_error(message: str) -> None:
    """Print an error message in red."""
    console.print(f"[bold red]✘ {message}[/bold red]")


def print_info(message: str) -> None:
    """Print an informational message in cyan."""
    console.print(f"[bold cyan]ℹ {message}[/bold cyan]")


def print_warning(message: str) -> None:
    """Print a warning message in yellow."""
    console.print(f"[bold yellow]⚠ {message}[/bold yellow]")


def confirm(message: str) -> bool:
    """Ask the user a yes/no question. Returns True only on an explicit 'y'/'yes'."""
    answer = Prompt.ask(f"[bold yellow]{message} (y/n)[/bold yellow]", default="n")
    return answer.strip().lower() in ("y", "yes")


def render_transactions_table(transactions: List[Dict[str, Any]], title: str = "Transactions") -> None:
    """Render a list of transactions as a Rich table."""
    if not transactions:
        console.print(Panel("[italic]No transactions to display.[/italic]", style="yellow"))
        return

    table = Table(title=title, show_lines=False, header_style="bold magenta")
    table.add_column("ID", justify="right", style="bold")
    table.add_column("Type", justify="center")
    table.add_column("Amount", justify="right")
    table.add_column("Category")
    table.add_column("Description")
    table.add_column("Date", justify="center")

    for tx in transactions:
        type_style = "green" if tx["type"] == "income" else "red"
        amount_display = format_currency(tx["amount"])
        table.add_row(
            str(tx["id"]),
            f"[{type_style}]{tx['type'].capitalize()}[/{type_style}]",
            f"[{type_style}]{amount_display}[/{type_style}]",
            tx["category"],
            tx["description"] or "-",
            tx["date"],
        )

    console.print(table)


def render_monthly_summary(summary: Dict[str, Any], year: int, month: int) -> None:
    """Render the monthly summary as a set of Rich panels."""
    month_name = f"{year:04d}-{month:02d}"

    if summary["total_transactions"] == 0:
        console.print(
            Panel(
                f"[italic]No transactions found for {month_name}.[/italic]",
                title="Monthly Summary",
                style="yellow",
            )
        )
        return

    overview = (
        f"[bold green]Total Income:[/bold green]  {format_currency(summary['total_income'])}\n"
        f"[bold red]Total Expense:[/bold red] {format_currency(summary['total_expense'])}\n"
        f"[bold cyan]Net Savings:[/bold cyan]   {format_currency(summary['net_savings'])}\n"
        f"[bold]Total Transactions:[/bold] {summary['total_transactions']}"
    )
    console.print(Panel(overview, title=f"Summary for {month_name}", style="bold blue"))

    highest_income = summary["highest_income"]
    highest_expense = summary["highest_expense"]

    income_amount_str = format_currency(highest_income["amount"]) if highest_income else "N/A"
    income_category_str = f" ({highest_income['category']})" if highest_income else ""
    expense_amount_str = format_currency(highest_expense["amount"]) if highest_expense else "N/A"
    expense_category_str = f" ({highest_expense['category']})" if highest_expense else ""

    highest_text = (
        f"[bold green]Highest Income:[/bold green]  {income_amount_str}{income_category_str}\n"
        f"[bold red]Highest Expense:[/bold red] {expense_amount_str}{expense_category_str}"
    )
    console.print(Panel(highest_text, title="Highs", style="bold magenta"))

    averages_text = (
        f"[bold green]Average Income:[/bold green]  {format_currency(summary['average_income'])}\n"
        f"[bold red]Average Expense:[/bold red] {format_currency(summary['average_expense'])}"
    )
    console.print(Panel(averages_text, title="Averages", style="bold white"))


def print_goodbye() -> None:
    """Print a farewell message."""
    console.print()
    console.print(Panel("[bold cyan]Thank you for using Personal Finance Manager. Goodbye![/bold cyan]", style="bold blue"))
