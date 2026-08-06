import tkinter as tk
from tkinter import messagebox

import api
import theme
from windows import Card, RoundedButton, FieldEntry, VaultMark


class LoginWindow:

    def __init__(self, root, on_login_success):

        self.root = root
        self.on_login_success = on_login_success

        self.frame = tk.Frame(root, bg=theme.BG)
        self.frame.pack(fill="both", expand=True)

        self.card = Card(self.frame, padding=28)
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=400, height=560)

        content = self.card.inner

        # -----------------------------
        # Header / signature mark
        # -----------------------------
        VaultMark(content, size=56).pack(pady=(0, 12))

        tk.Label(
            content,
            text="Welcome Back",
            bg=theme.SURFACE,
            fg=theme.TEXT,
            font=theme.FONT_DISPLAY
        ).pack()

        tk.Label(
            content,
            text="Sign in to your vault, or create a new account",
            bg=theme.SURFACE,
            fg=theme.TEXT_MUTED,
            font=theme.FONT_LABEL
        ).pack(pady=(4, 22))

        # -----------------------------
        # Fields
        # -----------------------------
        self.username_field = FieldEntry(content, "Username", icon="👤")
        self.username_field.pack(fill="x", pady=6)

        self.email_field = FieldEntry(content, "Email (register only)", icon="✉")
        self.email_field.pack(fill="x", pady=6)

        self.password_field = FieldEntry(content, "Password", icon="🔒", show="*")
        self.password_field.pack(fill="x", pady=6)

        # -----------------------------
        # Buttons
        # -----------------------------
        button_row = tk.Frame(content, bg=theme.SURFACE)
        button_row.pack(fill="x", pady=(24, 0))

        RoundedButton(
            button_row,
            text="Login",
            icon="🔓",
            command=self.login,
            width=170,
            height=42
        ).pack(side="left")

        RoundedButton(
            button_row,
            text="Register",
            icon="✨",
            command=self.register,
            width=170,
            height=42,
            variant="ghost"
        ).pack(side="right")

        self.status = tk.Label(
            content,
            text="",
            bg=theme.SURFACE,
            fg=theme.TEXT_FAINT,
            font=theme.FONT_SMALL
        )
        self.status.pack(pady=(16, 0))

    # ----------------------------
    # Login
    # ----------------------------

    def login(self):

        username = self.username_field.get().strip()
        password = self.password_field.get()

        if not username or not password:

            messagebox.showwarning(
                "Missing Data",
                "Enter username and password."
            )
            return

        self.status.config(text="Authenticating…", fg=theme.TEXT_MUTED)
        self.root.update_idletasks()

        response = api.login(
            username,
            password
        )

        if response.status_code == 200:

            self.status.config(text="Login successful.", fg=theme.TEAL)

            self.frame.destroy()

            self.on_login_success()

        else:

            try:
                detail = response.json()["detail"]
            except Exception:
                detail = response.text

            self.status.config(text="Login failed.", fg=theme.DANGER)

            messagebox.showerror(
                "Login Failed",
                detail
            )

    # ----------------------------
    # Register
    # ----------------------------

    def register(self):

        username = self.username_field.get().strip()
        email = self.email_field.get().strip()
        password = self.password_field.get()

        if not username or not email or not password:

            messagebox.showwarning(
                "Missing Data",
                "Fill all fields."
            )
            return

        response = api.register(
            username,
            email,
            password
        )

        if response.status_code in [200, 201]:

            messagebox.showinfo(
                "Success",
                "Registration Successful!\nNow login."
            )

            self.email_field.clear()
            self.password_field.clear()

            self.status.config(text="Account created — please log in.", fg=theme.TEAL)

        else:

            try:
                detail = response.json()["detail"]
            except Exception:
                detail = response.text

            self.status.config(text="Registration failed.", fg=theme.DANGER)

            messagebox.showerror(
                "Registration Failed",
                detail
            )
