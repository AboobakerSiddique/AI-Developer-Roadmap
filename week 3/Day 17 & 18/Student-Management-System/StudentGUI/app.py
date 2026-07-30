import tkinter as tk
from tkinter import ttk, messagebox
from api import add_student, get_students

import tkinter as tk
from tkinter import ttk, messagebox

from api import (
    add_student,
    get_students,
    update_student,
    delete_student
)

# ==========================
# Window
# ==========================

root = tk.Tk()

root.title("Student Management System")

root.geometry("1100x700")

root.minsize(950, 650)

root.configure(bg="#f5f5f5")

# ==========================
# Variables
# ==========================

selected_student_id = None

search_var = tk.StringVar()

status_var = tk.StringVar()

status_var.set("Ready")

# ==========================
# Style
# ==========================

total_students = tk.StringVar()

total_students.set("Students : 0")


style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Treeview",
    rowheight=28,
    font=("Segoe UI", 10)
)

style.configure(
    "Treeview.Heading",
    font=("Segoe UI", 10, "bold")
)

style.configure(
    "TButton",
    font=("Segoe UI", 10)
)

style.configure(
    "TLabel",
    font=("Segoe UI", 10)
)

# ==========================
# Main Frames
# ==========================

top_frame = ttk.Frame(root)

top_frame.pack(
    fill="x",
    padx=15,
    pady=10
)

middle_frame = ttk.Frame(root)

middle_frame.pack(
    fill="both",
    expand=True,
    padx=15
)

bottom_frame = ttk.Frame(root)

bottom_frame.pack(
    fill="x",
    padx=15,
    pady=10
)

# ==========================
# Title
# ==========================

title = ttk.Label(
    top_frame,
    text="🎓 Student Management System",
    font=("Segoe UI", 18, "bold")
)

title.pack(anchor="center")

# ==========================
# Search Frame
# ==========================

search_frame = ttk.LabelFrame(
    middle_frame,
    text="Search Student"
)

search_frame.pack(
    fill="x",
    pady=10
)

ttk.Label(
    search_frame,
    text="Name:"
).pack(
    side="left",
    padx=10,
    pady=10
)

search_entry = ttk.Entry(
    search_frame,
    textvariable=search_var,
    width=35
)

search_entry.pack(
    side="left"
)

# Buttons added later

# ==========================
# Form Frame
# ==========================

form_frame = ttk.LabelFrame(
    middle_frame,
    text="Student Details"
)

form_frame.pack(
    fill="x",
    pady=10
)

# ---------- Name ----------

ttk.Label(
    form_frame,
    text="Name"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky="w"
)

name_entry = ttk.Entry(
    form_frame,
    width=35
)

name_entry.grid(
    row=0,
    column=1,
    padx=10
)

# ---------- Age ----------

ttk.Label(
    form_frame,
    text="Age"
).grid(
    row=0,
    column=2,
    padx=10
)

age_entry = ttk.Entry(
    form_frame,
    width=15
)

age_entry.grid(
    row=0,
    column=3,
    padx=10
)

# ---------- Course ----------

ttk.Label(
    form_frame,
    text="Course"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=10,
    sticky="w"
)

course_entry = ttk.Entry(
    form_frame,
    width=35
)

course_entry.grid(
    row=1,
    column=1,
    padx=10
)

# ---------- Email ----------

ttk.Label(
    form_frame,
    text="Email"
).grid(
    row=1,
    column=2,
    padx=10
)

email_entry = ttk.Entry(
    form_frame,
    width=35
)

email_entry.grid(
    row=1,
    column=3,
    padx=10
)

# ==========================
# Table Frame
# ==========================

table_frame = ttk.Frame(
    middle_frame
)

table_frame.pack(
    fill="both",
    expand=True
)

columns = (
    "ID",
    "Name",
    "Age",
    "Course",
    "Email"
)

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

for col in columns:

    tree.heading(
    col,
    text=col,
    command=lambda c=col:
    sort_column(c, False)
)

tree.column(
    "ID",
    width=60,
    anchor="center"
)

tree.column(
    "Name",
    width=180
)

tree.column(
    "Age",
    width=70,
    anchor="center"
)

tree.column(
    "Course",
    width=180
)

tree.column(
    "Email",
    width=280
)

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=tree.yview
)

tree.configure(
    yscrollcommand=scrollbar.set
)

tree.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)

# ==========================
# Button Frame
# ==========================

button_frame = ttk.Frame(
    bottom_frame
)

button_frame.pack()

# Buttons will be added later

# ==========================
# Status Bar
# ==========================

status = ttk.Label(
    root,
    textvariable=status_var,
    relief="sunken",
    anchor="w"
)

status.pack(
    side="bottom",
    fill="x"
)



# ==========================================
# CLEAR FORM
# ==========================================

def clear_form():

    global selected_student_id

    selected_student_id = None

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    status_var.set("Form Cleared")


# ==========================================
# REFRESH TABLE
# ==========================================

def refresh():

    tree.delete(*tree.get_children())

    students = get_students()

    if isinstance(students, dict):

        messagebox.showerror(
            "Error",
            students.get("detail", "Unknown Error")
        )

        return

    for student in students:

        tree.insert(

            "",

            tk.END,

            values=(

                student["id"],

                student["name"],

                student["age"],

                student["course"],

                student["email"]

            )

        )

    status_var.set(f"{len(students)} Students Loaded")


# ==========================================
# SEARCH
# ==========================================

def search_student():

    keyword = search_var.get().lower()

    tree.delete(*tree.get_children())

    students = get_students()

    if isinstance(students, dict):

        return

    for student in students:

        if keyword in student["name"].lower():

            tree.insert(

                "",

                tk.END,

                values=(

                    student["id"],

                    student["name"],

                    student["age"],

                    student["course"],

                    student["email"]

                )

            )

    status_var.set("Search Completed")


# ==========================================
# LOAD SELECTED STUDENT
# ==========================================

def load_student(event):

    global selected_student_id

    selected = tree.focus()

    if not selected:

        return

    values = tree.item(selected)["values"]

    selected_student_id = values[0]

    clear_form()

    selected_student_id = values[0]

    name_entry.insert(0, values[1])

    age_entry.insert(0, values[2])

    course_entry.insert(0, values[3])

    email_entry.insert(0, values[4])

    status_var.set(

        f"Editing Student ID {selected_student_id}"

    )


tree.bind(

    "<Double-1>",

    load_student

)


# ==========================================
# ADD STUDENT
# ==========================================

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

            messagebox.showerror(

                "Error",

                response["detail"]

            )

            return

        messagebox.showinfo(

            "Success",

            "Student Added Successfully"

        )

        clear_form()

        refresh()

    except ValueError:

        messagebox.showerror(

            "Error",

            "Age must be a number"

        )
        
# ==========================================
# UPDATE STUDENT
# ==========================================

def edit_student():

    global selected_student_id

    if selected_student_id is None:

        messagebox.showwarning(
            "No Selection",
            "Double-click a student first."
        )
        return

    try:

        student = {
            "name": name_entry.get(),
            "age": int(age_entry.get()),
            "course": course_entry.get(),
            "email": email_entry.get()
        }

        response = update_student(
            selected_student_id,
            student
        )

        if isinstance(response, dict) and "detail" in response:

            messagebox.showerror(
                "Error",
                response["detail"]
            )
            return

        messagebox.showinfo(
            "Success",
            "Student Updated Successfully"
        )

        clear_form()

        refresh()

    except ValueError:

        messagebox.showerror(
            "Error",
            "Age must be a number."
        )


# ==========================================
# DELETE STUDENT
# ==========================================

def remove_student():

    global selected_student_id

    if selected_student_id is None:

        messagebox.showwarning(
            "No Selection",
            "Double-click a student first."
        )

        return

    confirm = messagebox.askyesno(

        "Delete Student",

        "Are you sure you want to delete this student?"

    )

    if not confirm:
        return

    response = delete_student(
        selected_student_id
    )

    if isinstance(response, dict) and "detail" in response:

        messagebox.showerror(

            "Error",

            response["detail"]

        )

        return

    messagebox.showinfo(

        "Deleted",

        "Student Deleted Successfully"

    )
    
def sort_column(col, reverse):

    data = [(tree.set(child, col), child)
            for child in tree.get_children("")]

    try:
        data.sort(
            key=lambda x: int(x[0]),
            reverse=reverse
        )
    except:
        data.sort(
            key=lambda x: x[0].lower(),
            reverse=reverse
        )

    for index, (_, child) in enumerate(data):

        tree.move(child, "", index)

    tree.heading(
        col,
        command=lambda:
        sort_column(col, not reverse)
    )

    clear_form()

    refresh()


# ==========================================
# BUTTONS
# ==========================================

ttk.Button(

    search_frame,

    text="Search",

    command=search_student

).pack(

    side="left",

    padx=10

)

ttk.Button(

    search_frame,

    text="Show All",

    command=refresh

).pack(

    side="left"

)


ttk.Button(

    button_frame,

    text="Add Student",

    command=save_student

).grid(

    row=0,

    column=0,

    padx=8,

    pady=10

)


ttk.Button(

    button_frame,

    text="Update",

    command=edit_student

).grid(

    row=0,

    column=1,

    padx=8

)


ttk.Button(

    button_frame,

    text="Delete",

    command=remove_student

).grid(

    row=0,

    column=2,

    padx=8

)


ttk.Button(

    button_frame,

    text="Clear Form",

    command=clear_form

).grid(

    row=0,

    column=3,

    padx=8

)


ttk.Button(

    button_frame,

    text="Refresh",

    command=refresh

).grid(

    row=0,

    column=4,

    padx=8

)


# ==========================================
# SHORTCUTS
# ==========================================

root.bind(

    "<Control-r>",

    lambda e: refresh()

)

root.bind(

    "<Escape>",

    lambda e: clear_form()

)


# ==========================================
# STARTUP
# ==========================================

refresh()

root.mainloop()