import requests

BASE_URL = "http://127.0.0.1:8001"


def get_students():
    response = requests.get(f"{BASE_URL}/students")
    response.raise_for_status()
    return response.json()


def add_student(student):
    response = requests.post(f"{BASE_URL}/students", json=student)
    response.raise_for_status()
    return response.json()


def delete_student(student_id):
    response = requests.delete(f"{BASE_URL}/students/{student_id}")
    response.raise_for_status()
    return response.json()