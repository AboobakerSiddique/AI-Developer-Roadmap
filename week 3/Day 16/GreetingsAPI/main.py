from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
class Address(BaseModel):
    street: str
    city: str
    pincode: str


class Student(BaseModel):
    name: str
    age: int
    course: str
    address: Address
    
@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student added successfully!",
        "student": student
    }