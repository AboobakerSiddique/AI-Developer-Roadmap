import json
data = '{"name":"Alex","age":20}'
student = json.loads(data)
print(student["age"])