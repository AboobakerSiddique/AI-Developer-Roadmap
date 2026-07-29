from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(
    title="Student Management API",
    description="A simple CRUD API built using FastAPI",
    version="1.0.0"
)


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=18, le=60)
    course: str = Field(min_length=2, max_length=50)
    email: EmailStr


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str
    email: EmailStr


students = []
next_id = 1


@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


@app.get("/students", response_model=List[StudentResponse])
def get_students():
    return students


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    global next_id

    new_student = {
        "id": next_id,
        **student.model_dump()
    }

    students.append(new_student)
    next_id += 1

    return new_student


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, updated: StudentCreate):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students[index] = {
                "id": student_id,
                **updated.model_dump()
            }
            return students[index]

    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students.pop(index)
            return {"message": "Student deleted successfully"}

    raise HTTPException(status_code=404, detail="Student not found")