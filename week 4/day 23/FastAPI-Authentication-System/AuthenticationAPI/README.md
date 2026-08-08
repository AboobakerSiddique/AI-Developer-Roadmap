# 🔐 Authentication API — FastAPI

> A complete JWT-based authentication REST API built with **FastAPI**, featuring secure password hashing, JWT authentication, protected routes, SQLAlchemy ORM, SQLite, environment-based configuration, logging, and user account management.

🚀 Built as part of my **AI Developer Roadmap** to develop practical backend and API development skills.

---

## 📖 Overview

This project is a complete backend authentication system built using **FastAPI**.

It implements the core authentication workflow used in modern applications:

```text
Registration
     ↓
Password Hashing
     ↓
Database
     ↓
Login
     ↓
Password Verification
     ↓
JWT Generation
     ↓
Protected API
     ↓
Authenticated User
```

The API is also consumed by a separate **Tkinter Desktop GUI**, allowing users to interact with the backend through a graphical interface instead of directly using API documentation.

---

# ✨ Features

## 🔐 Authentication

- 👤 User Registration
- 🔑 Password Hashing with bcrypt
- 🔒 Password Verification
- 🎫 JWT Access Token Generation
- ⏳ JWT Token Expiration
- 🛡 Protected Routes
- 🔑 Bearer Token Authentication
- 🚫 Invalid / Expired Token Handling

## 👤 User Management

- 👤 View Current User
- ✏️ Update Profile
- 🗑️ Delete Account
- ✅ Unique Username Validation
- ✅ Unique Email Validation
- 📋 Request Validation
- ❌ Proper Error Handling

## ⚙️ Configuration & Production Practices

- 🌱 Environment Variables
- 🔐 `.env` Configuration
- 🔑 Secret Key Management
- 📝 Application Logging
- 📦 Requirements Management
- 🚫 Sensitive Files excluded through `.gitignore`

## 📚 API

- ⚡ FastAPI REST API
- 📖 Swagger UI
- 📘 ReDoc
- 💉 Dependency Injection
- 🗄️ SQLAlchemy ORM
- 🗃️ SQLite Database

---

# 🛠 Tech Stack

| Category | Technology |
|---|---|
| Language | Python |
| Framework | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Password Hashing | Passlib + bcrypt |
| Authentication | JWT |
| JWT Library | python-jose |
| Configuration | python-dotenv |
| Server | Uvicorn |
| API Documentation | Swagger UI / ReDoc |
| Client | Tkinter Desktop GUI |

---

# 📂 Project Structure

```text
AuthenticationAPI/
│
├── auth.py              # Password hashing & JWT authentication
├── config.py            # Environment-based configuration
├── database.py          # Database configuration & sessions
├── logging_config.py    # Application logging configuration
├── models.py            # SQLAlchemy database models
├── routes.py            # API routes
├── schemas.py           # Pydantic schemas
├── main.py              # FastAPI application
│
├── requirements.txt     # Python dependencies
├── .gitignore           # Ignored files
├── .env                 # Local environment variables
└── README.md
```

> ⚠️ `.env` and the SQLite database are intentionally excluded from GitHub.

---

# 🔄 Authentication Flow

## Registration

```text
User
 │
 ▼
POST /register
 │
 ▼
Validate Input
 │
 ▼
Hash Password
 │
 ▼
bcrypt
 │
 ▼
Store User
 │
 ▼
SQLite Database
```

---

## Login

```text
User
 │
 ▼
POST /login
 │
 ▼
Find User
 │
 ▼
Verify Password
 │
 ▼
Generate JWT
 │
 ▼
Return Access Token
```

---

## Protected Request

```text
Desktop GUI
 │
 ▼
GET /me
 │
 ▼
Authorization: Bearer <JWT>
 │
 ▼
FastAPI
 │
 ▼
Decode JWT
 │
 ▼
Verify Signature
 │
 ▼
Check Expiration
 │
 ▼
Find User
 │
 ▼
Return User
```

---

# 📌 API Endpoints

## 🏠 General

| Method | Endpoint | Authentication | Description |
|---|---|---|---|
| GET | `/` | ❌ | API welcome message |

---

## 👤 Authentication

| Method | Endpoint | Authentication | Description |
|---|---|---|---|
| POST | `/register` | ❌ | Register a new user |
| POST | `/login` | ❌ | Login and receive JWT |

---

## 🔒 User Management

| Method | Endpoint | Authentication | Description |
|---|---|---|---|
| GET | `/me` | ✅ | Get current authenticated user |
| PUT | `/profile` | ✅ | Update current user's profile |
| DELETE | `/account` | ✅ | Delete current user's account |

> 🔑 Protected endpoints require a valid JWT Bearer token.

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
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

# 🔑 Using the JWT

After logging in, the client receives an access token.

Protected requests send:

```http
Authorization: Bearer <access_token>
```

For example:

```http
GET /me
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

The API verifies the token before allowing access.

---

# 🔐 Password Security

Passwords are **never stored directly** in the database.

Instead:

```text
Plain Password
      ↓
    bcrypt
      ↓
Salt + Hash
      ↓
SQLite
```

During login:

```text
Entered Password
      ↓
bcrypt Verification
      ↓
Stored Password Hash
      ↓
Match?
   ↙      ↘
 YES      NO
  ↓        ↓
Login    Reject
```

This means the original password does not need to be stored.

---

# ⚙️ Environment Variables

Sensitive configuration is stored in `.env`.

Example:

```env
DATABASE_URL=sqlite:///./users.db

SECRET_KEY=your-secret-key

JWT_SECRET=your-jwt-secret

API_KEY=your-api-key

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

The application loads these values through the configuration system.

### 🔒 Security

`.env` is included in `.gitignore` and should **never be committed to GitHub**.

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/AboobakerSiddique/FastAPI-Authentication-System.git
```

---

## 2️⃣ Navigate to API

```bash
cd FastAPI-Authentication-System
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell execution policy prevents activation, use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧪 Run Locally

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger can be used to test:

- Registration
- Login
- JWT authentication
- Protected routes
- Profile updates
- Account deletion

---

# 🖥️ Desktop GUI

This API is also connected to a separate **Tkinter Desktop GUI**.

```text
┌──────────────────────┐
│   Tkinter Desktop    │
│        GUI           │
└──────────┬───────────┘
           │
           │ HTTP Requests
           │ + JWT
           ▼
┌──────────────────────┐
│      FastAPI         │
│       REST API       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      SQLAlchemy      │
│        + SQLite      │
└──────────────────────┘
```

The GUI allows users to:

- Register
- Login
- View Dashboard
- View Profile
- Edit Profile
- Delete Account
- Logout

---

# ☁️ Deployment

This API is being prepared for deployment using **Render**.

### Production Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Build Command

```bash
pip install -r requirements.txt
```

### Deployment Architecture

```text
GitHub
   │
   ▼
Render
   │
   ▼
FastAPI
   │
   ▼
SQLAlchemy
   │
   ▼
SQLite
```

Environment variables such as:

```text
DATABASE_URL
SECRET_KEY
JWT_SECRET
API_KEY
ACCESS_TOKEN_EXPIRE_MINUTES
```

are configured directly in the Render dashboard rather than committed to GitHub.

> ⚠️ SQLite is being used here for learning and deployment practice. A production application would generally use a persistent database such as PostgreSQL.

---

# 🔐 Security Features

- 🔒 Passwords hashed using bcrypt
- 🚫 Plain-text passwords never stored
- 🎫 JWT tokens digitally signed
- ⏳ JWT expiration
- 🛡 Protected endpoints
- 🔑 Bearer authentication
- 🚫 Invalid/expired tokens rejected
- ✅ Duplicate username prevention
- ✅ Duplicate email prevention
- 🌱 Secrets stored through environment variables
- 🚫 `.env` excluded from Git
- 📝 Authentication events logged without exposing passwords or tokens

---

# 🧠 Concepts Learned

Through this project, I learned and implemented:

### Python

- Functions
- Modules
- Virtual Environments
- Environment Variables
- Exception Handling
- Logging

### FastAPI

- REST APIs
- Routing
- Request/Response Handling
- Dependency Injection
- Pydantic Validation
- HTTP Status Codes
- Error Handling
- OAuth2PasswordBearer
- Protected Routes
- Swagger Documentation
- ReDoc

### Database

- SQLite
- SQLAlchemy ORM
- Database Models
- Database Sessions
- CRUD Operations
- Querying
- Unique Constraints

### Authentication

- Authentication vs Authorization
- Password Hashing
- bcrypt
- Salt
- Hash Verification
- JWT
- Access Tokens
- Token Expiration
- Bearer Tokens
- Protected Endpoints

### Deployment

- GitHub Integration
- Environment Variables
- Build Commands
- Start Commands
- Deployment Logs
- Production Server Configuration

---

# 🚧 Current Limitations

This project intentionally focuses on authentication fundamentals.

It currently does not include:

- Refresh Tokens
- Password Reset
- Email Verification
- Role-Based Access Control
- Admin Permissions
- OAuth / Google Login
- Rate Limiting
- Automated Testing
- PostgreSQL
- Docker
- HTTPS configuration

---

# 🚀 Future Improvements

Planned improvements:

- 🔄 Refresh Token System
- 🔑 Change Password
- 📧 Email Verification
- 🔐 Forgot Password
- 👑 Role-Based Access Control
- 🛡️ Admin Dashboard
- 🚦 Rate Limiting
- 🧪 Automated Testing with Pytest
- 🐘 PostgreSQL
- 🐳 Docker
- ☁️ Production Deployment
- 🔑 OAuth / Google Authentication
- 🌐 React Web Frontend

---

# 🎯 Learning Outcome

This project helped me understand authentication as a complete system rather than just implementing a login endpoint.

I learned how:

```text
User
 ↓
Registration
 ↓
Password Hashing
 ↓
Database
 ↓
Login
 ↓
Password Verification
 ↓
JWT
 ↓
Bearer Token
 ↓
Protected API
 ↓
Authenticated User
```

I also learned how a separate desktop application can communicate with a REST API and handle authentication using JWT.

Most importantly, I gained practical experience debugging real API authentication problems involving:

- JWT tokens
- Authorization headers
- Token expiration
- JSON requests
- API responses
- Environment variables
- GUI ↔ API communication
- Configuration issues

---

# 📈 Part of My AI Developer Roadmap

This project is part of my structured journey toward becoming an **AI Developer**.

```text
Python
   ↓
Git & GitHub
   ↓
APIs
   ↓
FastAPI
   ↓
Databases
   ↓
Authentication
   ↓
Deployment
   ↓
Backend Engineering
   ↓
AI / LLM Development
```

---

# 🤝 Connect With Me

### GitHub

https://github.com/AboobakerSiddique

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It motivates me to continue building, learning, and documenting my journey toward becoming an **AI Engineer**.

---

## 🚀 Built. Tested. Deployed.

> *Learn consistently. Build real projects. Share your journey.*

---

### 📌 Project Status

**🟢 Development:** Complete  
**🟢 Authentication:** Complete  
**🟢 GUI Integration:** Complete  
**🟢 Configuration:** Complete  
**🟢 Logging:** Complete  
**🟡 Deployment:** In Progress  
**⚪ PostgreSQL:** Future  
**⚪ Automated Testing:** Future