import tkinter as tk

import theme
from login_window import LoginWindow
from dashboard import Dashboard


root = tk.Tk()

root.title("Vault — Authentication System")

root.geometry("520x640")

root.resizable(False, False)

theme.apply_theme(root)


def open_dashboard():

    Dashboard(root)


LoginWindow(
    root,
    open_dashboard
)

root.mainloop()
