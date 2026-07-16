# 👨‍💼 Employee Database Management System

A command-line Employee Database Management System built in Python that demonstrates CRUD operations, file handling, JSON, CSV, modular programming, and data processing.

---

## 📌 Features

* ➕ Add Employee
* 👀 View All Employees
* 🔍 Search Employee (by ID or Name)
* ✏️ Update Employee Details
* 🗑️ Delete Employee
* 📂 Load Existing Employee Data from JSON
* 💾 Save Employee Data to JSON
* 📄 Export Employee Data to CSV
* 🔤 Sort Employees by Name
* 💰 Sort Employees by Salary
* 📊 Display Employee Statistics

  * Total Employees
  * Average Salary

---

## 🛠️ Technologies Used

* Python 3
* JSON
* CSV
* File Handling
* Dictionaries
* Lists
* Functions
* Exception Handling
* `os` Module

---

## 📁 Project Structure

```text
EmployeeDatabase/
│
├── employee_database.py
├── employee_details.json
├── employees_details.csv
└── README.md
```

---

## 📚 Concepts Practiced

### Python Fundamentals

* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* Exception Handling

### File Handling

* Reading Files
* Writing Files
* JSON Serialization
* CSV Export

### Python Modules

* `json`
* `csv`
* `os`

### Data Processing

* Searching Records
* Updating Records
* Sorting Data
* Calculating Statistics

---

## ▶️ Menu

```text
Employee Database
-----------------
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Sort Employees
7. Statistics
8. Save to JSON
9. Export to CSV
10. Exit
```

---

## 🚀 How It Works

### Add Employee

Stores employee information including:

* Employee ID
* Name
* Department
* Salary

Duplicate employee IDs are automatically prevented.

---

### View Employees

Displays all employees in a clean, formatted layout.

---

### Search Employee

Search using:

* Employee ID
* Employee Name

---

### Update Employee

Allows updating:

* Department
* Salary

Existing values can be kept by leaving the input blank.

---

### Delete Employee

Deletes an employee using either:

* Employee ID
* Employee Name

---

### Save to JSON

Stores all employee records in:

```text
employee_details.json
```

using pretty formatting (`indent=4`).

---

### Load from JSON

When the program starts, previously saved employee records are automatically loaded from the JSON file.

The program also:

* Validates loaded data
* Ignores corrupted records
* Prevents duplicate employee IDs

---

### Export to CSV

Exports employee records to:

```text
employees_details.csv
```

making them compatible with spreadsheet applications like Microsoft Excel and Google Sheets.

---

### Sort Employees

Employees can be sorted by:

* Name (Alphabetically)
* Salary (Ascending)

---

### Statistics

Displays:

* Total number of employees
* Average employee salary

---

## 🧠 Skills Demonstrated

* CRUD (Create, Read, Update, Delete) Operations
* Data Validation
* Persistent Data Storage
* JSON Processing
* CSV Export
* Searching Algorithms
* Sorting Collections
* Error Handling
* Clean Function-Based Program Design

---

## 📖 Future Improvements

Potential enhancements include:

* Edit Employee Name
* Edit Employee ID
* Salary Range Search
* Department Filter
* Pagination for Large Employee Lists
* Auto-Save After Every Change
* Login Authentication
* SQLite Database Integration
* Graphical User Interface (Tkinter or PyQt)
* REST API Version using Flask or FastAPI

---

## 📸 Example Output

```text
Employee Database
-----------------
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Sort Employees
7. Statistics
8. Save to JSON
9. Export to CSV
10. Exit
```

---

## 🎯 Learning Outcome

This project combines multiple Python concepts into a practical CRUD application, reinforcing:

* File handling with JSON and CSV
* Data structures (lists and dictionaries)
* Modular programming with functions
* Input validation and exception handling
* Basic data management techniques commonly used in real-world software development
