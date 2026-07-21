# 📝 Quote Generator

A simple Python command-line application that fetches **random inspirational quotes** from a public API and displays them in the terminal.

This project was built as part of my **AI Developer Roadmap** to practice working with REST APIs, JSON responses, and the Python `requests` library.

---

## 🚀 Features

* 🎲 Fetch a random quote instantly
* 🌐 Uses a real REST API
* 📦 Parses JSON responses
* ⚠️ Handles network errors gracefully
* 🏗️ Modular project structure
* 🖥️ Simple menu-driven CLI

---

## 🛠️ Technologies Used

* Python 3
* requests
* REST API
* JSON

---

## 📂 Project Structure

```text
QuoteGenerator/
│
├── main.py
├── quote_api.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd QuoteGenerator
```

(Optional) Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Example:

```text
========================================
      RANDOM QUOTE GENERATOR
========================================

1. Get Random Quote
2. Exit

Enter your choice: 1

------------------------------------------------------------
"The only way to do great work is to love what you do."

— Steve Jobs
------------------------------------------------------------
```

---

## 🌐 API Used

This project uses the free public DummyJSON Quotes API:

https://dummyjson.com/quotes/random

No API key is required.

---

## 📚 Concepts Practiced

* Working with REST APIs
* HTTP GET requests
* JSON parsing
* Error handling using try/except
* Status code checking
* Functions and modular programming
* Importing custom modules
* Command-line application development

---

## 🔮 Future Improvements

* 📋 Copy quote to clipboard
* ❤️ Save favorite quotes
* 📂 Export quotes to a text file
* 🔍 Search quotes by author
* 🎭 Quote categories
* 🌍 Multiple quote APIs as fallback
* 🖥️ GUI version using Tkinter or CustomTkinter

---

## 👨‍💻 Author

**Aboobaker Siddique**

GitHub: https://github.com/AboobakerSiddique

---

## ⭐ Learning Outcome

This project helped me understand how Python applications communicate with external services using APIs. It strengthened my understanding of HTTP requests, JSON handling, modular programming, and building real-world command-line applications.
