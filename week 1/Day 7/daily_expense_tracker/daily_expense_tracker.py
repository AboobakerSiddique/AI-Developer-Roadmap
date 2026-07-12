import datetime
import os

folder = os.path.dirname(__file__)
file_path = os.path.join(folder, "expenses.txt")


def add_expense():
    now = datetime.datetime.now()

    try:
        expense_name = input("Enter the expense name: ").strip()

        if expense_name == "":
            print("Expense name cannot be empty.")
            return

        expense_amount = float(input("Enter the amount: ₹"))

        if expense_amount <= 0:
            print("Amount must be greater than zero.")
            return

        expense_date = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"{expense_date}|{expense_name}|{expense_amount}\n")

        print("✅ Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            expenses = file.readlines()

        if not expenses:
            print("\nNo expenses found.\n")
            return

        print("\n----------- Expenses -----------")

        for i, expense in enumerate(expenses, start=1):
            parts = expense.strip().split("|")

            if len(parts) != 3:
                continue

            print(f"{i}. Date    : {parts[0]}")
            print(f"   Expense : {parts[1]}")
            print(f"   Amount  : ₹{float(parts[2]):.2f}")
            print("-------------------------------")

    except FileNotFoundError:
        print("No expenses recorded yet.")


def total_expenses():
    total = 0

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) != 3:
                    continue

                total += float(parts[2])

        print(f"\nTotal Expenses: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expenses recorded yet.")


def delete_expense():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            expenses = file.readlines()

        if len(expenses) == 0:
            print("No expenses to delete.")
            return

        view_expenses()

        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)

            with open(file_path, "w", encoding="utf-8") as file:
                file.writelines(expenses)

            print("Deleted successfully!")
            print(removed.strip())

        else:
            print("Invalid expense number.")

    except (ValueError, FileNotFoundError):
        print("Operation failed.")


def search_expense():
    keyword = input("Enter expense name to search: ").lower().strip()

    if keyword == "":
        print("Search cannot be empty.")
        return

    found = False

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) != 3:
                    continue

                if keyword in parts[1].lower():
                    print(f"{parts[0]} | {parts[1]} | ₹{float(parts[2]):.2f}")
                    found = True

        if not found:
            print("No matching expense found.")

    except FileNotFoundError:
        print("No expenses recorded yet.")


def expense_count():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            expenses = file.readlines()

        print(f"Total number of expenses: {len(expenses)}")

    except FileNotFoundError:
        print("No expenses recorded yet.")


while True:

    print("\n====== Daily Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Search Expense")
    print("6. Expense Count")
    print("7. Exit")
    print("===================================")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            total_expenses()

        elif choice == 4:
            delete_expense()

        elif choice == 5:
            search_expense()

        elif choice == 6:
            expense_count()

        elif choice == 7:
            print("Thank you for using Daily Expense Tracker!")
            break

        else:
            print("Please enter a number between 1 and 7.")

    except ValueError:
        print("Please enter numbers only.")