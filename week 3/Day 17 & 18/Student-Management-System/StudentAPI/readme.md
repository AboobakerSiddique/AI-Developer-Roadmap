# 🎓 Student Management API

A beginner-friendly REST API built with **FastAPI** that demonstrates CRUD operations, request validation, response models, and automatic API documentation.

## 🚀 Features

- ➕ Add Student
- 📋 Get All Students
- 🔍 Get Student by ID
- ✏️ Update Student
- ❌ Delete Student
- ✅ Request Validation using Pydantic
- 📧 Email Validation
- 📚 Interactive Swagger Documentation

## 🛠 Tech Stack

- Python 3
- FastAPI
- Pydantic
- Uvicorn

## 📦 Installation

```bash
git clone https://github.com/yourusername/StudentAPI.git

cd StudentAPI

python -m venv .venv
```

### Windows

```bash
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run

```bash
uvicorn main:app --reload
```

## 🌐 Swagger Docs

```
http://127.0.0.1:8000/docs
```

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home |
| GET | /students | Get all students |
| GET | /students/{id} | Get student by ID |
| POST | /students | Add student |
| PUT | /students/{id} | Update student |
| DELETE | /students/{id} | Delete student |

## Example Request

```json
{
  "name": "Aboobaker",
  "age": 21,
  "course": "AI Developer",
  "email": "aboobaker@gmail.com"
}
```

## Learning Outcomes

- FastAPI Routing
- CRUD Operations
- Request Body Validation
- Response Models
- Path Parameters
- HTTP Status Codes
- Swagger Documentation
- REST API Design

## Future Improvements

- SQLite Database
- SQLAlchemy ORM
- JWT Authentication
- User Login
- Pagination
- Docker Support
- Unit Testing