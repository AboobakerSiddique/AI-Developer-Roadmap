# Week 2 – Day 9: Python Modules & Project Structure

## 📌 Overview

Today focused on learning how professional Python applications are organized using modules and multiple files. Instead of writing all code in a single script, I learned how to split functionality into reusable modules, import them into other files, and understand how Python locates and executes modules.

---

## 📚 Topics Covered

* Python Modules
* Why modules are important
* Creating and importing custom modules
* Different import styles

  * `import module`
  * `from module import function`
  * `import module as alias`
  * `from module import function as alias`
* Module Search Path (`sys.path`)
* Standard Library Modules
* `__name__ == "__main__"`
* Multi-file Python project structure

---

## 🛠️ Practical Exercises

### Greetings Module

Created a simple custom module and imported it into another Python file.

**Concepts learned:**

* Creating a reusable module
* Calling functions from another file
* Understanding how Python imports modules

---

### Standard Library Practice

Explored commonly used built-in modules:

* `math`
* `random`
* `datetime`
* `os`
* `sys`
* `time`

Practiced using their most common functions and understood real-world use cases.

---

### Multi-file Calculator Project

Built a calculator application using separate modules for each mathematical operation.

### Project Structure

```text
Calculator/
│
├── main.py
├── add.py
├── subtract.py
├── multiply.py
└── divide.py
```

### Features

* Addition
* Subtraction
* Multiplication
* Division
* Division by zero handling
* User-friendly menu
* Input validation
* Multiple calculations in one session

---

## 🧠 Key Concepts Learned

### What is a Module?

A module is a Python file (`.py`) containing reusable code that can be imported into other Python programs.

---

### Why Use Modules?

* Better code organization
* Easier debugging
* Improved readability
* Code reusability
* Professional project structure

---

### Module Search Path

Learned how Python searches for modules in the following order:

1. Current project directory
2. Installed packages
3. Python Standard Library
4. Directories listed in `sys.path`

---

### Standard Library

Understood that Python includes many built-in modules that can be used without installing additional packages.

---

### `__name__ == "__main__"`

Learned how Python determines whether a file is:

* executed directly
* imported as a module

This allows the same file to be both reusable and independently executable.

---

## 🎯 Skills Gained

* Creating custom modules
* Importing modules correctly
* Using aliases with imports
* Understanding Python's module search mechanism
* Working with built-in Python libraries
* Organizing projects into multiple files
* Building reusable code
* Structuring Python applications like professional developers

---

## 💡 Key Takeaways

* Every Python file is a module.
* Splitting projects into multiple files improves maintainability and scalability.
* The Python Standard Library provides many powerful tools out of the box.
* `__name__ == "__main__"` prevents unwanted code execution when modules are imported.
* Writing modular code is an essential skill for software development and AI engineering.

---

## 📈 Progress

**Week 2 Progress**

* ✅ Day 8 – Object-Oriented Programming (Part 1)
* ✅ Day 9 – Python Modules & Project Structure

---

**Next Topic:** Data Structures & Algorithms (Arrays) + Python Packages and larger multi-file project organization.
