from fastapi import FastAPI

from database import Base, engine
from routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Authentication API",
    description="Week 4 Day 2 - Password Hashing",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Authentication API Running"
    }


app.include_router(router)