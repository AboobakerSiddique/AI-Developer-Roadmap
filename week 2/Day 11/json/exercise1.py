import json

student = {
    "name": "Creator",
    "age": 21,
    "skills": ["Python", "Git", "OOP"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    data = json.load(file)

print(f"Name: {data['name']}")
print(f"Age: {data['age']}")
print(f"Skills: {', '.join(data['skills'])}")


