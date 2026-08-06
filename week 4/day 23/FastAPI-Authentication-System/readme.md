# 🔐 FastAPI Authentication System

A complete JWT Authentication System built with **FastAPI**, **SQLAlchemy**, **SQLite**, and a **Tkinter Desktop GUI**.
This project demonstrates modern backend authentication concepts including secure password hashing, JWT authentication, protected routes, dependency injection, and complete user account management through a desktop client.

---

## 🚀 Features

### Authentication

- ✅ User Registration
- ✅ User Login
- ✅ Password Hashing (bcrypt)
- ✅ JWT Token Authentication
- ✅ Protected Routes

### User Management

- ✅ View Current User
- ✅ Update Profile
- ✅ Delete Account
- ✅ Unique Username Validation
- ✅ Unique Email Validation

### Desktop GUI

- ✅ Register
- ✅ Login
- ✅ Dashboard
- ✅ View Profile
- ✅ Edit Profile
- ✅ Delete Account
- ✅ Logout

---

# 🖥 Screenshots

## Login

![Login](screenshots/login.png)

---

## Dashboard

![Dashboard](screenshots/dashboard.png)

---

## Edit Profile

![Edit Profile](screenshots/edit_profile.png)

---

# 🎥 Demo

## 📹 Project Demo

Watch the complete authentication flow in action:

- ✅ User Registration
- ✅ User Login
- ✅ JWT Authentication
- ✅ View Profile
- ✅ Update Profile
- ✅ Delete Account
- ✅ Logout

🎬 **Demo Video:**

https://github.com/AboobakerSiddique/FastAPI-Authentication-System/screenshots/test.mp4

---

## 🏗 Project Structure

### Backend

```text
AuthenticationAPI/

│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── routes.py
├── users.db
├── requirements.txt
└── README.md
```

### Desktop GUI

```text
AuthenticationGUI/

│
├── app.py
├── api.py
├── config.py
├── dashboard.py
├── login_window.py
├── profile_window.py
├── requirements.txt
└── README.md
```

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- Passlib
- bcrypt
- Python-JOSE
- Pydantic
- Uvicorn

## Frontend

- Tkinter
- ttk
- Requests

---

# 🔐 API Endpoints

| Method | Endpoint | Description |
|----------|------------|----------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT |
| GET | `/me` | View current user |
| PUT | `/profile` | Update profile |
| DELETE | `/account` | Delete account |

---

# 🔄 Authentication Flow

```text
User

↓

Register

↓

Password Hashing

↓

SQLite Database

↓

Login

↓

Password Verification

↓

JWT Generated

↓

Desktop GUI Stores Token

↓

Protected APIs

↓

Current User

↓

Update / Delete Profile
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/AboobakerSiddique/FastAPI-Authentication-System.git
```

Navigate into the project

```bash
cd FastAPI-Authentication-System
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run API

```bash
uvicorn main:app --reload
```

Run Desktop GUI

```bash
python app.py
```

---

# 📚 Concepts Covered

- REST APIs
- CRUD Operations
- SQLite
- SQLAlchemy ORM
- JWT Authentication
- Password Hashing
- Dependency Injection
- OAuth2PasswordBearer
- Request Validation
- Error Handling
- API Consumption
- Desktop GUI Development

---

# 📈 Future Improvements

- Change Password
- Refresh Tokens
- Forgot Password
- Email Verification
- Profile Picture Upload
- Admin Dashboard
- Role Based Access Control
- Web Frontend (React)

---

# 🎯 Learning Outcome

This project helped me understand how authentication works from end to end:

- Secure password storage
- JWT creation and verification
- Protected API routes
- CRUD operations
- Database integration
- Desktop client communicating with REST APIs

---

# 👨‍💻 Author

**Aboobaker Siddique**

Electronics & Communication Engineering Graduate

Currently learning:
- Python
- FastAPI
- SQLAlchemy
- AI Development
- Backend Engineering

---

⭐ If you found this project useful, consider giving it a star!