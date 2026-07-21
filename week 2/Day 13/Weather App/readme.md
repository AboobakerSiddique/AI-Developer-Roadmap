# 🌤️ Weather App

A Python command-line application that retrieves **real-time weather information** for any city using the **WeatherAPI.com REST API**.

This project was built as part of my **AI Developer Roadmap** to practice working with REST APIs, HTTP requests, API authentication, JSON parsing, and modular Python programming.

---

## 🚀 Features

* 🌍 Search current weather by city name
* 🌡️ Display current temperature
* 🤗 Feels-like temperature
* 💧 Humidity
* 🌬️ Wind speed
* 📈 Atmospheric pressure
* ☁️ Current weather condition
* ⚠️ Handles invalid city names
* 🔐 Uses API key authentication
* 🏗️ Clean modular project structure

---

## 🛠️ Technologies Used

* Python 3
* Requests
* REST API
* WeatherAPI.com
* JSON

---

## 📂 Project Structure

```text
WeatherApp/
│
├── main.py
├── weather_api.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/WeatherApp.git
```

Move into the project:

```bash
cd WeatherApp
```

Create a virtual environment (recommended):

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

## 🔑 API Key Setup

1. Create a free account at **https://www.weatherapi.com/**
2. Copy your API key from the dashboard.
3. Open `config.py`.
4. Replace:

```python
API_KEY = "YOUR_WEATHERAPI_KEY"
```

with your own API key.

Example:

```python
API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
BASE_URL = "https://api.weatherapi.com/v1/current.json"
```

> **Important:** Never upload your real API key to GitHub.

---

## 📄 .gitignore

Create a `.gitignore` file containing:

```gitignore
config.py
.venv/
__pycache__/
```

Then create a `config_example.py`:

```python
API_KEY = "YOUR_WEATHERAPI_KEY"
BASE_URL = "https://api.weatherapi.com/v1/current.json"
```

This allows others to use your project without exposing your private API key.

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Example:

```text
===== WEATHER APP =====

1. Check Weather
2. Exit

Enter choice: 1

Enter city name: London

=============================================
         CURRENT WEATHER
=============================================
City        : London
Country     : United Kingdom
Temperature : 15.1°C
Feels Like  : 15.1°C
Humidity    : 77%
Pressure    : 1028 hPa
Wind Speed  : 10.8 km/h
Condition   : Sunny
=============================================
```

---

## 📚 Concepts Practiced

* REST APIs
* HTTP GET requests
* API authentication using API keys
* Query parameters
* JSON parsing
* Nested dictionaries
* Exception handling
* Modular programming
* Functions
* Command-line applications

---

## 🔮 Future Improvements

* 🌅 Sunrise & sunset information
* 📍 Auto-detect current location
* ⭐ Save favourite cities
* 📅 7-day weather forecast
* 🌡️ Celsius/Fahrenheit toggle
* 🖥️ GUI version using CustomTkinter
* 📊 Weather history
* 🌎 Multiple language support

---

## 👨‍💻 Author

**Aboobaker Siddique**

GitHub: https://github.com/AboobakerSiddique

---

## ⭐ Learning Outcome

Through this project, I learned how to integrate third-party REST APIs into Python applications, authenticate requests using API keys, work with query parameters, process nested JSON responses, implement exception handling, and organize code using a modular project structure. These are essential skills for building real-world applications that consume external services.
