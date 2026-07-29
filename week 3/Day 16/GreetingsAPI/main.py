from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title="Greeting API",
    description="A beginner FastAPI project demonstrating routes, path parameters, and query parameters.",
    version="1.0.0"
)

# ---------------- HOME ----------------

@app.get("/")
def home():
    return {
        "message": "Welcome to Greeting API 🚀"
    }


# ---------------- ABOUT ----------------

@app.get("/about")
def about():
    return {
        "project": "Greeting API",
        "developer": "Aboobaker Siddique",
        "framework": "FastAPI",
        "version": "1.0"
    }


# ---------------- CONTACT ----------------

@app.get("/contact")
def contact():
    return {
        "github": "https://github.com/AboobakerSiddique",
        "email": "example@email.com"
    }


# ---------------- STATUS ----------------

@app.get("/status")
def status():
    return {
        "status": "Running",
        "server": "FastAPI"
    }


# ---------------- MOTIVATION ----------------

@app.get("/motivation")
def motivation():
    return {
        "quote": "Consistency beats motivation."
    }


# ---------------- SKILLS ----------------

@app.get("/skills")
def skills():
    return {
        "skills": [
            "Python",
            "SQL",
            "REST API",
            "FastAPI"
        ]
    }


# ---------------- PATH PARAMETERS ----------------

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }


@app.get("/hello/{name}")
def hello(name: str):
    return {
        "message": f"Hello, {name}! 👋"
    }


@app.get("/square/{number}")
def square(number: int):
    return {
        "number": number,
        "square": number ** 2
    }


@app.get("/cube/{number}")
def cube(number: int):
    return {
        "number": number,
        "cube": number ** 3
    }


@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "sum": a + b
    }


@app.get("/multiply/{a}/{b}")
def multiply_path(a: int, b: int):
    return {
        "product": a * b
    }


# ---------------- QUERY PARAMETERS ----------------

@app.get("/search")
def search(name: str):
    return {
        "search_result": f"Searching for {name}"
    }


@app.get("/welcome")
def welcome(name: str = "Guest"):
    return {
        "message": f"Welcome {name}"
    }


@app.get("/multiply")
def multiply_query(a: int, b: int):
    return {
        "product": a * b
    }


@app.get("/discount")
def discount(price: float, discount: float):
    final_price = price - (price * discount / 100)

    return {
        "original_price": price,
        "discount": f"{discount}%",
        "final_price": round(final_price, 2)
    }


@app.get("/bmi")
def bmi(weight: float, height: float):
    bmi_value = weight / (height ** 2)

    return {
        "BMI": round(bmi_value, 2)
    }


@app.get("/profile")
def profile(name: Optional[str] = None):
    if name:
        return {
            "message": f"Hello {name}"
        }

    return {
        "message": "Hello Guest"
    }


@app.get("/user-detail/{user_id}")
def user_detail(user_id: int, detail: bool = False):
    return {
        "user_id": user_id,
        "detail": detail
    }