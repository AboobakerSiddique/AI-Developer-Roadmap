import tkinter as tk
from tkinter import messagebox
from api import add_student, get_students

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x500")

# -----------------------------
# Name
# -----------------------------
tk.Label(root, text="Name").pack(pady=(10, 0))
name_entry = tk.Entry(root, width=40)
name_entry.pack()

# -----------------------------
# Age
# -----------------------------
tk.Label(root, text="Age").pack(pady=(10, 0))
age_entry = tk.Entry(root, width=40)
age_entry.pack()

# -----------------------------
# Course
# -----------------------------
tk.Label(root, text="Course").pack(pady=(10, 0))
course_entry = tk.Entry(root, width=40)
course_entry.pack()

# -----------------------------
# Email
# -----------------------------
tk.Label(root, text="Email").pack(pady=(10, 0))
email_entry = tk.Entry(root, width=40)
email_entry.pack()

# -----------------------------
# Student List
# -----------------------------
student_list = tk.Listbox(root, width=80, height=12)
student_list.pack(pady=20)


# -----------------------------
# Refresh Student List
# -----------------------------
def refresh():
    student_list.delete(0, tk.END)

    students = get_students()

    # If API returned an error
    if isinstance(students, dict):
        messagebox.showerror("API Error", str(students))
        return

    for student in students:
        student_list.insert(
            tk.END,
            f"ID: {student['id']} | "
            f"{student['name']} | "
            f"Age: {student['age']} | "
            f"{student['course']} | "
            f"{student['email']}"
        )


# -----------------------------
# Add Student
# -----------------------------
def save_student():
    try:
        student = {
            "name": name_entry.get(),
            "age": int(age_entry.get()),
            "course": course_entry.get(),
            "email": email_entry.get()
        }

        response = add_student(student)

        if isinstance(response, dict) and "detail" in response:
            messagebox.showerror("Error", str(response["detail"]))
            return

        messagebox.showinfo("Success", "Student Added Successfully!")

        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        course_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

        refresh()

    except ValueError:
        messagebox.showerror("Error", "Age must be a number.")


# -----------------------------
# Buttons
# -----------------------------
tk.Button(
    root,
    text="Add Student",
    width=20,
    command=save_student
).pack(pady=5)

tk.Button(
    root,
    text="Refresh Students",
    width=20,
    command=refresh
).pack()

# -----------------------------
# Initial Load
# -----------------------------
refresh()

root.mainloop()