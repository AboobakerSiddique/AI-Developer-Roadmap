import json
import csv
import os

employees = []

def load_from_json():
    if os.path.exists('employee_details.json'):
        try:
            with open('employee_details.json', 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            try:
                                employee_id = int(item['id'])
                                name = str(item['name'])
                                department = str(item['department'])
                                salary = int(item['salary'])
                                if not any(emp['id'] == employee_id for emp in employees):
                                    employees.append({
                                        'id': employee_id,
                                        'name': name,
                                        'department': department,
                                        'salary': salary
                                    })
                            except (ValueError, KeyError, TypeError):
                                continue
        except (json.JSONDecodeError, IOError):
            print('Warning: could not load employee_details.json.')


def print_employees(emp_list):
    if not emp_list:
        print('No employees to display.')
        return

    print('\nEmployees:')
    for emp in emp_list:
        print(f'ID: {emp["id"]}')
        print(f'Name: {emp["name"]}')
        print(f'Department: {emp["department"]}')
        print(f'Salary: {emp["salary"]}')
        print('-' * 20)


def add_employee():
    try:
        employee_id = int(input('enter your employee id: '))
        if any(emp['id'] == employee_id for emp in employees):
            print('Employee ID already exists.')
            return
        name = input('enter your name: ').strip()
        department = input('enter your department: ').strip()
        salary = int(input('enter your salary: '))
    except ValueError:
        print('enter a valid id or salary !!!')
        return

    employees.append({
        'id': employee_id,
        'name': name,
        'department': department,
        'salary': salary
    })
    print('Employee added successfully!')


def view_employees():
    print_employees(employees)


def search_employee():
    if not employees:
        print('No employees to search.')
        return

    search_term = input('Enter employee ID or name to search: ').strip()
    if not search_term:
        print('Search term cannot be empty.')
        return

    if search_term.isdigit():
        employee_id = int(search_term)
        matches = [emp for emp in employees if emp['id'] == employee_id]
    else:
        matches = [emp for emp in employees if emp['name'].lower() == search_term.lower()]

    if not matches:
        print('No matching employee found.')
        return

    print_employees(matches)


def update_employee():
    if not employees:
        print('No employees to update.')
        return

    search_term = input('Enter employee ID or name to update: ').strip()
    if not search_term:
        print('Search term cannot be empty.')
        return

    if search_term.isdigit():
        employee_id = int(search_term)
        matches = [emp for emp in employees if emp['id'] == employee_id]
    else:
        matches = [emp for emp in employees if emp['name'].lower() == search_term.lower()]

    if not matches:
        print('No matching employee found.')
        return

    if len(matches) > 1:
        print('Multiple employees found:')
        for emp in matches:
            print(f"ID: {emp['id']}, Name: {emp['name']}")
        selected_id = input('Enter the exact employee ID to update: ').strip()
        if not selected_id.isdigit():
            print('Invalid ID selection.')
            return
        employee_id = int(selected_id)
        matches = [emp for emp in matches if emp['id'] == employee_id]
        if not matches:
            print('No matching employee found for the selected ID.')
            return

    employee = matches[0]
    new_department = input(f'Enter new department (leave blank to keep "{employee["department"]}"): ').strip()
    new_salary = input(f'Enter new salary (leave blank to keep "{employee["salary"]}"): ').strip()

    if new_department:
        employee['department'] = new_department
    if new_salary:
        try:
            employee['salary'] = int(new_salary)
        except ValueError:
            print('enter a valid salary !!!')
            return

    print('Employee updated successfully.')


def delete_employee():
    global employees

    if not employees:
        print('No employees to delete.')
        return

    search_term = input('Enter employee ID or name to delete: ').strip()
    if not search_term:
        print('Search term cannot be empty.')
        return

    initial_count = len(employees)

    if search_term.isdigit():
        employee_id = int(search_term)
        employees = [emp for emp in employees if emp['id'] != employee_id]
    else:
        employees = [emp for emp in employees if emp['name'].lower() != search_term.lower()]

    if len(employees) < initial_count:
        print('Employee deleted successfully.')
    else:
        print('No matching employee found to delete.')


def sort_employees():
    if not employees:
        print('No employees to sort.')
        return

    print('1. Sort by name')
    print('2. Sort by salary')
    choice = input('Enter your choice (1/2): ').strip()

    if choice == '1':
        employees.sort(key=lambda emp: emp['name'].lower())
        print('Employees sorted by name.')
    elif choice == '2':
        employees.sort(key=lambda emp: emp['salary'])
        print('Employees sorted by salary.')
    else:
        print('enter a valid choice !!!')
        return

    print_employees(employees)


def display_statistics():
    if not employees:
        print('No employees available.')
        return

    total = len(employees)
    average = sum(emp['salary'] for emp in employees) / total
    print(f'Total employees: {total}')
    print(f'Average salary: {average:.2f}')


def save_to_json():
    with open('employee_details.json', 'w') as file:
        json.dump(employees, file, indent=4)
    print('JSON saved successfully.')


def export_to_csv():
    if not employees:
        print('No employees to export.')
        return

    fieldnames = ['id', 'name', 'department', 'salary']
    with open('employees_details.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees)
    print('CSV exported successfully.')

load_from_json()

while True:
    print('''
          Employee Database
-----------------
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Sort Employees
7. Statistics
8. Save to JSON
9. Export to CSV
10. Exit
          ''')
    
    try:
        choice = int(input('enter your choice (1/2/3/4/5/6/7/8/9/10): '))
    except ValueError:
        print('enter a valid choice !!!')
        continue

    if choice == 1:
        add_employee()
    elif choice == 2:
        view_employees()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        update_employee()
    elif choice == 5:
        delete_employee()
    elif choice == 6:
        sort_employees()
    elif choice == 7:
        display_statistics()
    elif choice == 8:
        save_to_json()
    elif choice == 9:
        export_to_csv()
    elif choice == 10:
        print('Exiting employee data')
        break
    else:
        print('enter a valid choice !!!')
    
    