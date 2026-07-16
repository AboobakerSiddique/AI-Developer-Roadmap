import json

with open("student_dump().json",'r') as file:
    student = json.load(file)
    
print(student)
print(student["name"])