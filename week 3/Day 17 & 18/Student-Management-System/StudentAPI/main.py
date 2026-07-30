from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    version="2.0.0"
)


@app.get("/")
def home():
    return {"message": "Student Management API using SQLite"}


@app.get("/students", response_model=List[schemas.StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)


@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):

    student = crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(404, "Student not found")

    return student


@app.post(
    "/students",
    response_model=schemas.StudentResponse,
    status_code=201
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):

    return crud.create_student(db, student)


@app.put(
    "/students/{student_id}",
    response_model=schemas.StudentResponse
)
def update_student(
    student_id: int,
    updated: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):

    student = crud.update_student(
        db,
        student_id,
        updated
    )

    if student is None:
        raise HTTPException(404, "Student not found")

    return student


@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = crud.delete_student(
        db,
        student_id
    )

    if student is None:
        raise HTTPException(404, "Student not found")

    return {"message": "Student deleted successfully"}