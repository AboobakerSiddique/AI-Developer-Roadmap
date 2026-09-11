# Fitscope — AI Resume Analyzer

Fitscope is an AI-powered resume analysis application that evaluates a candidate's compatibility with a specific job description.

Instead of relying only on keyword matching, Fitscope uses an LLM to semantically compare the candidate's experience, skills, and qualifications against the requirements of a target role and produces a structured compatibility report.

## 🌐 Live Demo

**Live Application:** https://frontend-ten-fitscope.vercel.app/

---

## ✨ Features

### 📄 Resume & Job Description Analysis

Upload documents as PDFs or provide their content directly as text.

Fitscope accepts:

* Resume / CV
* Job Description

The application processes both inputs and evaluates the candidate against the target role.

### 🎯 Compatibility Score

Generates an overall compatibility score from **0–100%** representing how closely the candidate's profile matches the job requirements.

### ✅ Matched Skills

Identifies relevant skills, technologies, tools, and qualifications that appear in both the candidate's resume and the job description.

### ❌ Missing Skills

Highlights important requirements from the job description that are not demonstrated in the candidate's resume.

### 💪 Strengths & Weaknesses

Provides contextual feedback about the candidate's strongest qualifications and relevant gaps.

### 📊 Requirement Match Breakdown

Fitscope goes beyond a single score by breaking the job description into individual requirements.

Each requirement receives a status such as:

* **Strong Match**
* **Partial Match**
* **No Match**

The application also provides a short explanation describing why the candidate received that status.

### 💡 AI Recommendation

Generates a concise recommendation summarizing the candidate's overall suitability for the role.

---

## 🧠 How It Works

```text
                ┌──────────────────┐
                │   Resume / CV    │
                └────────┬─────────┘
                         │
                         │
                ┌────────▼─────────┐
                │ Job Description  │
                └────────┬─────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Document Parsing   │
              │      / Text Input    │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │      FastAPI         │
              │      Backend         │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │      LangChain       │
              │   Analysis Pipeline  │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │     Gemini LLM       │
              │  Semantic Analysis   │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Pydantic Structured  │
              │       Output         │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Compatibility Report │
              └──────────────────────┘
```

---

## 🏗️ Architecture

Fitscope follows a simple separation between the frontend, backend, LLM orchestration, and structured output layers.

```text
Next.js Frontend
       │
       ▼
FastAPI Backend
       │
       ▼
LangChain
       │
       ▼
Gemini
       │
       ▼
Pydantic Schema
       │
       ▼
Structured JSON Response
       │
       ▼
Next.js Results UI
```

### Frontend

The frontend is responsible for:

* Resume input
* Job description input
* PDF upload interface
* Loading states
* Error handling
* Compatibility report visualization
* Requirement match visualization

### Backend

FastAPI handles:

* API requests
* Input validation
* PDF/text processing
* LLM invocation
* Structured response generation
* Error handling

### AI Layer

LangChain manages communication with Gemini and converts the model response into a predefined Pydantic structure.

This prevents the application from depending on unpredictable free-form LLM responses.

---

## 🛠️ Tech Stack

### Frontend

* **Next.js**
* **React**
* **TypeScript**
* **Tailwind CSS**

### Backend

* **Python**
* **FastAPI**
* **Pydantic**
* **Uvicorn**

### AI / LLM

* **LangChain**
* **Google Gemini**
* **Gemini 3.5 Flash**
* **Structured Output**

### Document Processing

* **pypdf**

### Development Tools

* Git
* GitHub
* VS Code
* Postman / Swagger UI

---

## 📦 Project Structure

```text
fitscope/
│
├── frontend/
│   ├── src/
│   │   └── app/
│   │       └── page.tsx
│   │
│   ├── package.json
│   ├── package-lock.json
│   ├── tsconfig.json
│   └── ...
│
├── backend/
│   ├── schemas/
│   │   └── resume_analysis.py
│   │
│   ├── main.py
│   ├── requirements.txt
│   ├── .gitignore
│   └── .env
│
└── README.md
```

---

## 📋 Structured Output

The AI response is validated using a Pydantic schema rather than being returned as unrestricted text.

Example structure:

```json
{
  "candidate_name": "Arjun Menon",
  "matched_skills": [
    "Python",
    "FastAPI",
    "REST APIs",
    "PostgreSQL",
    "SQLAlchemy",
    "JWT"
  ],
  "missing_skills": [
    "Redis",
    "Celery",
    "Kubernetes"
  ],
  "strengths": [
    "Strong Python backend foundation",
    "Experience building REST APIs",
    "Good understanding of API authentication"
  ],
  "weaknesses": [
    "Limited experience with distributed systems",
    "No demonstrated Kubernetes experience"
  ],
  "match_score": 84,
  "recommendation": "Strong candidate for the role with some gaps in distributed infrastructure."
}
```

This provides a predictable structure that the frontend can reliably consume.

---

## 🔍 Analysis Components

### Skill Matching

The model compares the candidate's demonstrated skills against the requirements of the job description.

### Skill Gap Detection

Important requirements that are not demonstrated in the resume are identified as potential gaps.

### Contextual Evaluation

The system considers the context surrounding skills and experience instead of simply counting matching keywords.

### Requirement-Level Evaluation

Individual requirements are evaluated independently to provide more useful feedback than a single overall score.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd fitscope
```

---

## Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### Environment Variables

Create a `.env` file inside the `backend` directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

**Never commit your `.env` file or expose your API key publicly.**

---

### Start the Backend

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Open a new terminal and navigate to:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:3000
```

---

## 🔌 API

### `POST /analyze`

Analyzes a resume against a job description.

#### Request

```json
{
  "resume": "Candidate resume text...",
  "job_description": "Target job description..."
}
```

#### Response

```json
{
  "candidate_name": "Candidate Name",
  "matched_skills": [],
  "missing_skills": [],
  "strengths": [],
  "weaknesses": [],
  "match_score": 85,
  "recommendation": "..."
}
```

### PDF Analysis

The PDF workflow accepts:

```text
Resume PDF
+
Job Description PDF
```

The backend extracts selectable text from the documents before sending the content through the existing AI analysis pipeline.

Scanned/image-only PDFs without extractable text are rejected rather than producing unreliable analysis.

---

## 🔐 Validation & Error Handling

Fitscope includes validation at multiple stages.

### Input Validation

* Resume content cannot be empty
* Job description cannot be empty
* Minimum input length is enforced
* PDF uploads are validated
* Unsupported/invalid documents are rejected

### AI Output Validation

Gemini's response is validated against the Pydantic `ResumeAnalysis` schema.

The match score is constrained to:

```text
0 ≤ score ≤ 100
```

### API Error Handling

The backend returns appropriate errors when:

* Input is invalid
* PDF text cannot be extracted
* AI analysis fails
* Structured output is invalid

API keys and sensitive document contents are not included in application logs.

---

## 🎨 Design

Fitscope uses a minimal document-analysis interface rather than a conventional AI dashboard.

The design focuses on:

* Clear typography
* Strong visual hierarchy
* Minimal color usage
* High readability
* Generous spacing
* Clear document states
* Simple data visualization

The interface intentionally avoids excessive gradients, glassmorphism, decorative AI imagery, and unnecessary animations.

---

## 🧪 Example Use Case

A candidate wants to apply for a Python Backend Developer position.

They provide:

**Resume**

```text
Python
FastAPI
REST APIs
PostgreSQL
SQLAlchemy
JWT
Docker
Pytest
```

**Job Description**

```text
Python
FastAPI
PostgreSQL
SQLAlchemy
Redis
Celery
Docker
Kubernetes
Pytest
```

Fitscope can identify:

```text
Strong Matches
├── Python
├── FastAPI
├── PostgreSQL
├── SQLAlchemy
├── Docker
└── Pytest

Missing
├── Redis
├── Celery
└── Kubernetes
```

The user can then understand **what they already qualify for and which requirements represent gaps**.

---

## ⚠️ Limitations

Fitscope is an AI-assisted analysis tool and should not be treated as an automated hiring decision system.

Current limitations include:

* AI-generated scores are estimates, not objective measurements.
* Resume quality affects analysis quality.
* Scanned PDFs without extractable text are not currently supported.
* The system cannot verify whether information in a resume is truthful.
* Hiring decisions should not be based solely on the generated score.

---

## 🔮 Future Improvements

Potential future improvements include:

* Resume improvement suggestions
* ATS keyword analysis
* Resume-to-JD comparison history
* Resume tailoring for a specific job
* Exportable compatibility reports
* OCR support for scanned documents
* Authentication and saved analyses
* Job application tracking
* Multiple resume comparison

---

## 🎯 Learning Objectives

This project was built to gain practical experience with:

* LangChain
* LLM application development
* Gemini API integration
* Structured LLM output
* Pydantic schemas
* FastAPI API development
* PDF text extraction
* Frontend/backend integration
* AI response validation
* Error handling
* Building deployable AI applications


---

## 📄 License

This project is available under the **MIT License**.

See the `LICENSE` file for details.

---

## ⭐ If You Found This Useful

If you find Fitscope useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## Author

**Aboobaker Siddique**

AI Application Developer | Python Backend Developer | Generative AI

* GitHub: https://github.com/AboobakerSiddique
* LinkedIn: https://www.linkedin.com/in/aboobaker-siddique-ba4a66333/
* Portfolio: https://portfolio-ten-theta-gasws6e4rg.vercel.app/
