import tkinter as tk

from login_window import LoginWindow
from dashboard import Dashboard
import tkinter as tk
from tkinter import ttk

style = ttk.Style()

print(style.theme_names())

style.theme_use("vista")

root = tk.Tk()

root.title("Authentication System")

root.geometry("500x450")

root.resizable(False, False)


def open_dashboard():

    Dashboard(root)


LoginWindow(
    root,
    open_dashboard
)

root.mainloop()