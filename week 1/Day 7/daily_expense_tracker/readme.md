# 💰 Daily Expense Tracker

## 📖 Project Overview
The **Daily Expense Tracker** is a command-line Python application that helps users record and manage their daily expenses. It allows users to add expenses, view all recorded expenses, calculate the total amount spent, search for specific expenses, delete expenses, and keep track of the total number of recorded expenses. All data is stored permanently in a text file so that expenses are available even after the program is closed.

---

## ✨ Features

- ➕ Add a new expense
- 📋 View all recorded expenses
- 💰 Calculate total expenses
- 🔍 Search expenses by name
- 🗑️ Delete an expense
- 📊 Display total number of expenses
- 💾 Automatic file storage using `expenses.txt`
- ⚠️ Input validation and exception handling

---

## 🛠️ Technologies Used

- Python 3
- File Handling
- Functions
- Loops
- Conditional Statements
- Exception Handling (`try` / `except`)
- `datetime` Module
- `os` Module

---

## 📂 Project Structure

```
daily_expense_tracker/
│
├── daily_expense_tracker.py
├── expenses.txt
└── README.md
```

---

## 📁 Expense Storage Format

Each expense is stored in the following format:

```
Date | Expense Name | Amount
```

Example:

```
2026-07-12 08:30:12|Chicken|330
2026-07-12 09:10:45|Petrol|500
2026-07-12 10:20:31|Coffee|80
```

---

## 📋 Menu

```
====== Daily Expense Tracker ======

1. Add Expense
2. View Expenses
3. Total Expenses
4. Delete Expense
5. Search Expense
6. Expense Count
7. Exit

===================================
```

---

## 🧠 Concepts Practiced

- Modular Programming
- Function Design
- File Reading & Writing
- Working with Text Files
- String Manipulation
- Lists
- User Input Validation
- Exception Handling
- Date & Time Management
- File Path Management using `os.path`

---

## 🚀 Learning Outcome

Through this project, I learned how to:

- Design a complete command-line application.
- Store data permanently using text files.
- Read, write, update, and delete records from a file.
- Validate user input and handle runtime errors.
- Organize code into reusable functions.
- Use Python's `datetime` and `os` modules effectively.
- Build a real-world application without relying on tutorials.

---

## 🔮 Future Improvements

- Expense Categories (Food, Travel, Shopping, Bills, etc.)
- Monthly & Yearly Expense Reports
- Expense Editing Feature
- Sort Expenses by Date or Amount
- Category-wise Expense Summary
- Export Expenses to CSV or Excel
- Graphical User Interface (GUI)
- Database Integration (SQLite)

---

## 🎯 Project Status

✅ Completed as part of **Week 1 – Day 7** of my **AI Application Developer Roadmap**.

This project demonstrates my understanding of Python fundamentals, file handling, modular programming, and exception handling by building a practical real-world application.