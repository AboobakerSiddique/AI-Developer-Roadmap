import csv
employees = [
    ["Name", "Age", "Department"],
    ["Alex", 21, "ECE"],
    ["John", 23, "CSE"],
    ["Sarah", 22, "ME"]
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerows(employees)
    
with open('employees.csv','r') as file:
    reader = csv.reader(file)
    header = next(reader)
    
    for row in reader:
        print(f"Name: {row[0]}")
        print(f"Age: {row[1]}")
        print(f"Course: {row[2]}")
        print('-----------------')