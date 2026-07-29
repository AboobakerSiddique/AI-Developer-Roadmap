# 🎓 Student Management System

A full-stack Python Student Management System built using **FastAPI** as the backend and **Tkinter** as the desktop frontend.

The application demonstrates how a frontend communicates with a REST API using HTTP requests while performing complete CRUD (Create, Read, Update, Delete) operations.

---

## 📸 Demo

> Add your demo GIF or video here.

Example:

![Demo](demo.gif)

or

https://github.com/yourusername/Student-Management-System/assets/xxxxx/demo.mp4

---

# ✨ Features

## Backend (FastAPI)

- REST API
- Create Student
- View Students
- Get Student by ID
- Update Student
- Delete Student
- Request Validation using Pydantic
- Automatic Swagger Documentation

---

## Desktop GUI (Tkinter)

- Add Student
- View Students
- Refresh Student List
- Error Handling
- User Friendly Interface

---

# 🛠 Tech Stack

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic
- Requests
- Tkinter

---

# 📁 Project Structure

```
Student-Management-System
│
├── StudentAPI
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── StudentGUI
│   ├── app.py
│   ├── api.py
│   ├── requirements.txt
│   └── README.md
│
├── LICENSE
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/AboobakerSiddique/Student-Management-System.git
```

```
cd Student-Management-System
```

---

# Backend Setup

```
cd StudentAPI
```

Create virtual environment

```
python -m venv .venv
```

Activate

Windows

```
.venv\Scripts\activate
```

Install packages

```
pip install -r requirements.txt
```

Run server

```
uvicorn main:app --reload --port 8001
```

API Documentation

```
http://127.0.0.1:8001/docs
```

---

# Frontend Setup

Open another terminal

```
cd StudentGUI
```

Create virtual environment

```
python -m venv .venv
```

Activate

```
.venv\Scripts\activate
```

Install packages

```
pip install -r requirements.txt
```

Run GUI

```
python app.py
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home |
| GET | /students | Get all students |
| GET | /students/{id} | Get student |
| POST | /students | Create student |
| PUT | /students/{id} | Update student |
| DELETE | /students/{id} | Delete student |

---

# Example Request

```json
{
    "name":"Alex",
    "age":22,
    "course":"Python",
    "email":"alex@gmail.com"
}
```

---

# Example Response

```json
{
    "id":1,
    "name":"Alex",
    "age":22,
    "course":"Python",
    "email":"alex@gmail.com"
}
```

---

# Learning Outcomes

This project helped me understand:

- REST APIs
- HTTP Methods
- FastAPI
- CRUD Operations
- Request Validation
- Pydantic Models
- JSON
- API Documentation
- Desktop GUI Development
- Frontend ↔ Backend Communication

---

# Future Improvements

- SQLite Database
- SQLAlchemy ORM
- JWT Authentication
- Login System
- Search Students
- Pagination
- Export CSV
- Docker Support
- Cloud Deployment
- React Frontend

---

# Author

**Aboobaker Siddique**

GitHub:

https://github.com/AboobakerSiddique

LinkedIn:

(Add your LinkedIn URL)

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.