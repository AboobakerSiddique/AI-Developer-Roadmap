# 🔐 Authentication API using FastAPI

> A secure user authentication system built with **FastAPI**, featuring **password hashing**, **JWT authentication**, **protected routes**, and **SQLite** database.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

This project demonstrates a complete authentication workflow using **FastAPI**.

It includes secure user registration, password hashing using **bcrypt**, JWT token generation, token verification, and protected API endpoints.

This project was built as part of my **AI Developer Roadmap** to strengthen my backend development and authentication fundamentals.

---

# ✨ Features

- 👤 User Registration
- 🔑 Password Hashing with bcrypt
- 🔒 Secure Password Verification
- 🎫 JWT Access Token Generation
- 🛡 Protected Routes
- 🗄 SQLite Database
- ⚡ SQLAlchemy ORM
- 📚 Swagger API Documentation
- ❌ Proper Error Handling

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Password Hashing | Passlib + bcrypt |
| Authentication | JWT (python-jose) |
| API Documentation | Swagger UI |

---

# 📂 Project Structure

```text
AuthenticationAPI/
│
├── auth.py              # Password hashing & JWT functions
├── database.py          # Database configuration
├── models.py            # SQLAlchemy models
├── routes.py            # API routes
├── schemas.py           # Pydantic schemas
├── main.py              # FastAPI application
├── users.db             # SQLite database
├── requirements.txt
└── README.md
```

---

# 🔄 Authentication Flow

```text
User Registers
       │
       ▼
Password Hashed (bcrypt)
       │
       ▼
Store User in SQLite
       │
──────────────────────────────
       │
User Logs In
       │
       ▼
Verify Password
       │
       ▼
Generate JWT Token
       │
       ▼
Return Access Token
       │
──────────────────────────────
       │
Protected Route
       │
       ▼
Authorization: Bearer <JWT>
       │
       ▼
Verify JWT
       │
       ▼
Access Granted
```

---

# 📌 API Endpoints

## 🏠 Home

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API Welcome Message |

---

## 👤 Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT |

---

## 🔒 Protected

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/profile` | Access protected user profile |

---

# 📥 Example Requests

## Register

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "mypassword123"
}
```

---

## Login

```json
{
  "username": "john",
  "password": "mypassword123"
}
```

---

## Successful Login Response

```json
{
  "access_token": "eyJhbGcOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AuthenticationAPI.git
```

```bash
cd AuthenticationAPI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate

```powershell
.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Server

```bash
uvicorn main:app --reload
```

---

# 📖 API Documentation

Swagger UI

```text
http://127.0.0.1:8000/docs
```

ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🔐 Security Features

- Passwords are hashed using **bcrypt**
- Plain-text passwords are **never stored**
- JWT tokens are digitally signed
- Protected endpoints require authentication
- Invalid or expired tokens are rejected
- Duplicate usernames and emails are prevented

---


# 🎯 Learning Outcomes

Through this project, I learned:

- FastAPI fundamentals
- SQLAlchemy ORM
- SQLite database integration
- Password hashing with bcrypt
- JWT authentication
- Protected API routes
- API testing with Swagger
- Authentication workflow

---

# 🚧 Future Improvements

- Refresh Tokens
- Role-Based Access Control (RBAC)
- Email Verification
- Password Reset
- Environment Variables (.env)
- Docker Support
- Unit Testing
- PostgreSQL Integration

---

# 🤝 Connect With Me

**GitHub**

https://github.com/AboobakerSiddique

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It motivates me to continue building and documenting my journey toward becoming an AI Engineer.

---

## 🚀 Built as part of my AI Developer Roadmap

> *"Learn consistently. Build real projects. Share your journey."*