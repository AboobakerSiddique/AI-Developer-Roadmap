import tkinter as tk
from tkinter import messagebox

import api
import theme
from windows import Card, RoundedButton, FieldEntry


class ProfileWindow:

    def __init__(self, root, refresh_callback):

        self.refresh_callback = refresh_callback

        self.window = tk.Toplevel(root)

        self.window.title("Edit Profile")

        self.window.geometry("400x380")

        self.window.configure(bg=theme.BG)

        self.window.resizable(False, False)

        card = Card(self.window, padding=22)
        card.pack(fill="both", expand=True, padx=16, pady=16)

        content = card.inner

        tk.Label(
            content,
            text="Edit Profile",
            bg=theme.SURFACE,
            fg=theme.TEXT,
            font=theme.FONT_TITLE
        ).pack(anchor="w", pady=(0, 4))

        tk.Label(
            content,
            text="Update your account details",
            bg=theme.SURFACE,
            fg=theme.TEXT_MUTED,
            font=theme.FONT_LABEL
        ).pack(anchor="w", pady=(0, 18))

        user = api.get_me().json()

        self.username_field = FieldEntry(content, "Username", icon="👤")
        self.username_field.pack(fill="x", pady=6)
        self.username_field.set(user["username"])

        self.email_field = FieldEntry(content, "Email", icon="✉")
        self.email_field.pack(fill="x", pady=6)
        self.email_field.set(user["email"])

        button_row = tk.Frame(content, bg=theme.SURFACE)
        button_row.pack(fill="x", pady=(24, 0))

        RoundedButton(
            button_row,
            text="Cancel",
            command=self.window.destroy,
            width=160,
            height=40,
            variant="ghost"
        ).pack(side="left")

        RoundedButton(
            button_row,
            text="Save Changes",
            icon="💾",
            command=self.save,
            width=160,
            height=40
        ).pack(side="right")

        self.status = tk.Label(
            content,
            text="",
            bg=theme.SURFACE,
            fg=theme.TEXT_FAINT,
            font=theme.FONT_SMALL
        )
        self.status.pack(pady=(14, 0))

    # -----------------------------

    def save(self):

        response = api.update_profile(

            self.username_field.get(),

            self.email_field.get()

        )

        if response.status_code == 200:

            messagebox.showinfo(
                "Success",
                "Profile Updated."
            )

            self.refresh_callback()

            self.window.destroy()

        else:

            self.status.config(text="Update failed.", fg=theme.DANGER)

            messagebox.showerror(
                "Error",
                response.text
            )
