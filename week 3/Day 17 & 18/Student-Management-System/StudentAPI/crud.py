from sqlalchemy.orm import Session

import models
import schemas


def get_students(db: Session):
    return db.query(models.Student).all()


def get_student(db: Session, student_id: int):
    return (
        db.query(models.Student)
        .filter(models.Student.id == student_id)
        .first()
    )


def create_student(db: Session, student: schemas.StudentCreate):

    db_student = models.Student(**student.model_dump())

    db.add(db_student)

    db.commit()

    db.refresh(db_student)

    return db_student


def update_student(
    db: Session,
    student_id: int,
    updated_student: schemas.StudentUpdate
):

    student = get_student(db, student_id)

    if student is None:
        return None

    student.name = updated_student.name
    student.age = updated_student.age
    student.course = updated_student.course
    student.email = updated_student.email

    db.commit()

    db.refresh(student)

    return student


def delete_student(db: Session, student_id: int):

    student = get_student(db, student_id)

    if student is None:
        return None

    db.delete(student)

    db.commit()

    return student