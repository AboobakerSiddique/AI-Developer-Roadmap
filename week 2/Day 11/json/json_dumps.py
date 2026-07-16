import json

student = {
    "name": "Creator",
    "age": 21,
    "course": "ECE"
}

dumps = json.dumps(student)
print(dumps) 