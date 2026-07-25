# 💰 Personal Finance Manager

A polished, production-quality command-line application for tracking personal
income and expenses, built entirely with Python's standard library and
[Rich](https://github.com/Textualize/rich) for a beautiful terminal UI.

---

## 📖 Project Overview

Personal Finance Manager is a single-user CLI tool that lets you log income
and expenses, search and edit past entries, generate monthly financial
summaries, and export your data to JSON or CSV — all backed by a local
SQLite database. No external services, no accounts, no internet connection
required.

---

## ✨ Features

- **Add Income / Add Expense** — record transactions with amount, category,
  and an optional description. The date is stamped automatically.
- **View Transactions** — browse every transaction in a color-coded Rich
  table, sorted newest first.
- **Search Transactions** — case-insensitive partial matching across
  category, description, and type.
- **Update Transaction** — edit only the fields you choose to change; the
  rest stay untouched.
- **Delete Transaction** — remove an entry by ID, with a confirmation
  prompt to prevent accidents.
- **Monthly Summary** — total income, total expense, net savings, highest
  income/expense, averages, and transaction count, displayed in Rich panels.
- **Export to JSON** — pretty-printed dump of all transactions.
- **Export to CSV** — spreadsheet-friendly export with headers.
- **Input Validation** — rejects negative/zero amounts, empty categories,
  overly long descriptions, and invalid menu selections.
- **Robust Logging** — every start, exit, add, update, delete, and error is
  written to `logs/app.log`.
- **Crash-Resistant** — SQLite errors, JSON/CSV errors, invalid input, and
  `Ctrl+C` are all handled gracefully; the program never crashes outright.

---

## 📸 Screenshots

> _Add screenshots or terminal recordings of the main menu, transaction
> table, and monthly summary panels here once you've run the app locally._

```
========== PERSONAL FINANCE MANAGER ==========
  1  Add Income
  2  Add Expense
  3  View Transactions
  4  Search Transactions
  5  Update Transaction
  6  Delete Transaction
  7  Monthly Summary
  8  Export JSON
  9  Export CSV
 10  Exit
```

---

## 🛠 Installation

### 1. Clone or download the project

```bash
git clone <your-repo-url>
cd PersonalFinanceManager
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

- **macOS / Linux**
  ```bash
  source .venv/bin/activate
  ```
- **Windows (PowerShell)**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Instructions

```bash
python main.py
```

The SQLite database (`data/finance.db`) and log file (`logs/app.log`) are
created automatically on first run — no manual setup needed.

---

## 📁 Folder Structure

```
PersonalFinanceManager/
├── main.py                  # Application entry point and menu loop
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .gitignore
├── data/
│   ├── finance.db            # SQLite database (auto-created)
│   ├── transactions.json     # JSON export output
│   └── transactions.csv      # CSV export output
├── logs/
│   └── app.log                # Application log file (auto-created)
└── modules/
    ├── database.py            # SQLite connection & CRUD operations
    ├── transaction.py         # Business logic layer (validation + DB)
    ├── reports.py              # Monthly summary calculations
    ├── export.py                # JSON / CSV export logic
    ├── validation.py           # Centralized input validation
    ├── utils.py                  # Logging, paths, date/currency helpers
    └── ui.py                       # Rich-based CLI presentation layer
```

---

## 🧰 Technologies

- **Python 3.10+** (developed and tested with 3.12/3.13)
- **SQLite3** — embedded relational database, no server required
- **Rich** — terminal formatting (tables, panels, rules, colored text)
- **JSON / CSV** — built-in export formats
- **pathlib**, **datetime**, **logging** — standard library utilities

---

## 💡 Example Output

**Adding an expense:**

```
Add Expense
Amount: 42.50
Category: Groceries
Description (optional): Weekly shopping
✔ Expense added successfully (ID 7).
```

**Monthly Summary:**

```
╭──────────── Summary for 2026-07 ────────────╮
│ Total Income:  $3,200.00                     │
│ Total Expense: $1,180.45                     │
│ Net Savings:   $2,019.55                     │
│ Total Transactions: 14                       │
╰───────────────────────────────────────────────╯
```

---

## 🚀 Future Improvements

- Multi-currency support with live exchange rates
- Recurring transactions (subscriptions, rent, salary)
- Budget limits per category with alerts
- Data visualization (charts) via a terminal plotting library
- Multi-user profiles
- Encrypted database option

---

## 📄 License

This project is released under the MIT License. See `LICENSE` for details
(or add one if distributing this project).

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes with clear messages
4. Push to your branch and open a Pull Request

Please keep new code PEP 8-compliant, add type hints and docstrings, and
avoid duplicating existing logic in `modules/`.
