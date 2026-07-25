import sqlite3

connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

employees = [
    ("Alex",22,"Developer",45000),
    ("John",24,"Designer",50000),
    ("Sarah",21,"HR",40000),
    ("David",26,"Manager",70000)
]

cursor.executemany("""
INSERT INTO employees(name, age, department, salary)
VALUES (?, ?, ?, ?)
""", employees)

connection.commit()

print("Employees added successfully!\n")

cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()