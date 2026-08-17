# AI CLI Assistant

A lightweight command-line AI assistant built with **Python** and the **Google Gemini API**.

This project was built as part of **Day 31 — OpenAI & Gemini APIs** of my AI Developer Roadmap. It focuses on understanding how real applications communicate with LLM providers, manage conversation context, handle API failures, and securely manage API credentials.

## 🚀 Features

* 🤖 Gemini LLM integration
* 💬 Interactive CLI chat
* 🧠 Multi-turn conversation history
* 🔐 Secure API key management with `.env`
* ⚠️ API error handling
* 🔄 Basic retry handling for rate limits
* 🚪 `exit` command
* 🧹 `clear` command to reset conversation history
* 📦 Python virtual environment support

---

## 🛠️ Tech Stack

* **Python**
* **Google Gemini API**
* **Google GenAI Python SDK**
* **python-dotenv**

---

## 📁 Project Structure

```text
ai-cli-assistant/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### `main.py`

Contains the complete CLI application, including:

* Gemini client initialization
* Conversation history
* API requests
* Error handling
* Retry logic
* CLI interaction

### `.env`

Stores the Gemini API key locally.

### `requirements.txt`

Contains the Python dependencies required by the project.

---

# ⚙️ Setup

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd ai-cli-assistant
```

## 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\activate
```

You should see:

```text
(.venv)
```

at the beginning of your terminal prompt.

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure the API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

The application loads the key using `python-dotenv`.

**Never hard-code your API key inside `main.py`.**

❌ Don't do:

```python
GEMINI_API_KEY = "your-secret-key"
```

✅ Instead:

```env
GEMINI_API_KEY=your-secret-key
```

---

## 5. Run the application

```bash
python main.py
```

You should see:

```text
==================================================
           AI CLI ASSISTANT
==================================================

Type 'exit' to quit.
Type 'clear' to clear conversation history.

You:
```

---

# 💬 Usage

### Ask a question

```text
You: Explain recursion in simple terms.

AI: Recursion is a programming technique...
```

### Test conversation history

```text
You: My name is Alex.

AI: Nice to meet you, Alex!

You: What's my name?

AI: Your name is Alex.
```

The assistant can use previous messages because the application sends the conversation history as context to the model.

---

# 🧹 Clear Conversation

Type:

```text
clear
```

The current conversation history is removed from memory.

```text
Conversation history cleared.
```

After clearing, the model no longer receives the previous conversation as context.

---

# 🚪 Exit

Type:

```text
exit
```

The application terminates.

---

# 🧠 How Conversation History Works

The application maintains a conversation history in memory:

```text
User message
     ↓
Add to history
     ↓
Send history + new message
     ↓
Gemini
     ↓
AI response
     ↓
Add response to history
```

Conceptually:

```text
┌─────────────────────────────┐
│      Conversation History   │
├─────────────────────────────┤
│ User: My name is Alex       │
│ AI: Nice to meet you        │
│ User: I am learning Python  │
│ AI: That's great!           │
│ User: What am I learning?   │
└──────────────┬──────────────┘
               ↓
          Gemini API
               ↓
           AI Response
```

This demonstrates an important concept in LLM application development:

> **The application manages conversation context; the LLM does not automatically remember previous API requests.**

---

# ⚠️ Error Handling

The application handles common API problems such as:

### Authentication errors

```text
401
```

Possible cause:

* Missing API key
* Invalid API key

### Rate limits / quota

```text
429
```

The application performs limited retries with increasing delays.

### Resource/model errors

```text
404
```

Possible cause:

* Invalid model
* Invalid resource

### Unexpected errors

Other API failures are caught and reported instead of immediately crashing the application.

---

# 🔄 Retry Strategy

For retryable rate-limit errors, the application uses a simple exponential backoff:

```text
Attempt 1 → wait 1 second
Attempt 2 → wait 2 seconds
Attempt 3 → wait 4 seconds
```

This prevents the application from continuously sending requests when the API is temporarily unavailable or rate-limited.

---

# 🔐 Security

API credentials are stored in:

```text
.env
```

and `.env` is excluded through:

```text
.gitignore
```

Example:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

**Never commit API keys to GitHub.**

If an API key is accidentally exposed, revoke it and generate a new one.

---

# 📚 Concepts Practiced

This project applies the concepts learned throughout Day 31:

* API keys
* Environment variables
* SDKs
* LLM providers
* Model selection
* API requests
* API responses
* Error handling
* HTTP/API error concepts
* Rate limits
* Quotas
* Retry strategies
* Tokens
* Context windows
* Conversation history
* Context management
* Provider-specific SDK behavior

---

# 🔮 Current Limitations

This is an educational project, not a production-ready assistant.

Currently:

* Conversation history exists only in memory.
* Closing the application deletes the conversation.
* There is no database.
* There is no authentication system.
* There is no web interface.
* Context history is not automatically summarized.
* There is no persistent long-term memory.
* There is no RAG system.

These limitations are intentional because the project is focused on understanding the fundamentals of LLM API integration.

---

# 🚧 Future Improvements

Possible future upgrades include:

```text
CLI Assistant
     │
     ├── Persistent conversation storage
     │
     ├── SQLite/PostgreSQL
     │
     ├── Conversation summarization
     │
     ├── Context-window management
     │
     ├── FastAPI backend
     │
     ├── Web UI
     │
     ├── Authentication
     │
     ├── RAG
     │
     └── Multiple LLM providers
```

The eventual goal is to move from a simple CLI application toward a more complete **production-style AI application architecture**.

---

# 🎓 Learning Outcome

By completing this project, I practiced the fundamental workflow of an LLM-powered application:

```text
User
 ↓
Python Application
 ↓
Conversation / Context Management
 ↓
LLM API
 ↓
Model
 ↓
Response
 ↓
Application
 ↓
User
```

The project also demonstrates why an AI developer needs to understand more than simply calling an LLM API — **API security, model selection, context management, token usage, rate limits, and error handling are all part of building reliable AI applications.**

---

## 📌 Part of AI Developer Roadmap

**Week 5 — Generative AI & LLM Fundamentals**

**Day 31 — OpenAI & Gemini APIs**

Project:

> **AI CLI Assistant**
