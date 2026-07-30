import requests

BASE_URL = "http://127.0.0.1:8001"


def get_students():
    try:
        response = requests.get(f"{BASE_URL}/students")
        return response.json()
    except Exception as e:
        return {"detail": str(e)}


def add_student(student):
    try:
        response = requests.post(
            f"{BASE_URL}/students",
            json=student
        )
        return response.json()
    except Exception as e:
        return {"detail": str(e)}


def update_student(student_id, student):
    try:
        response = requests.put(
            f"{BASE_URL}/students/{student_id}",
            json=student
        )
        return response.json()
    except Exception as e:
        return {"detail": str(e)}


def delete_student(student_id):
    try:
        response = requests.delete(
            f"{BASE_URL}/students/{student_id}"
        )
        return response.json()
    except Exception as e:
        return {"detail": str(e)}