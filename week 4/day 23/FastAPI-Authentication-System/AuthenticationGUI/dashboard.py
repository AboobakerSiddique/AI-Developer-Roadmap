import tkinter as tk
from tkinter import messagebox

import api
import config
import theme
from windows import Card, RoundedButton, Avatar, StatusDot


class Dashboard:

    def __init__(self, root):

        self.root = root

        self.frame = tk.Frame(root, bg=theme.BG)
        self.frame.pack(fill="both", expand=True, padx=24, pady=24)

        self.action_width = 472  # 520 window - 24*2 padding

        # -----------------------------
        # Header: avatar + name + status
        # -----------------------------
        header = tk.Frame(self.frame, bg=theme.BG)
        header.pack(fill="x", pady=(0, 18))

        self.avatar = Avatar(header, initials="?", size=56)
        self.avatar.pack(side="left")

        text_col = tk.Frame(header, bg=theme.BG)
        text_col.pack(side="left", padx=(14, 0))

        self.title = tk.Label(
            text_col,
            text="Welcome",
            bg=theme.BG,
            fg=theme.TEXT,
            font=theme.FONT_DISPLAY
        )
        self.title.pack(anchor="w")

        status_row = tk.Frame(text_col, bg=theme.BG)
        status_row.pack(anchor="w", pady=(2, 0))

        self.status_dot = StatusDot(status_row, color=theme.TEAL, size=8)
        self.status_dot.pack(side="left")

        tk.Label(
            status_row,
            text="Session active",
            bg=theme.BG,
            fg=theme.TEXT_MUTED,
            font=theme.FONT_LABEL
        ).pack(side="left", padx=(4, 0))

        # -----------------------------
        # Profile information card
        # -----------------------------
        self.info_card = Card(self.frame, padding=18)
        self.info_card.pack(fill="x", pady=(0, 18))

        tk.Label(
            self.info_card.inner,
            text="PROFILE INFORMATION",
            bg=theme.SURFACE,
            fg=theme.ACCENT,
            font=theme.FONT_LABEL
        ).pack(anchor="w", pady=(0, 10))

        self.id_label = self._make_info_row(self.info_card.inner, "ID")
        self.username_label = self._make_info_row(self.info_card.inner, "Username")
        self.email_label = self._make_info_row(self.info_card.inner, "Email")

        # -----------------------------
        # Actions
        # -----------------------------
        actions = tk.Frame(self.frame, bg=theme.BG)
        actions.pack(fill="x")

        RoundedButton(
            actions, text="Refresh Profile", icon="🔄",
            command=self.refresh, width=self.action_width, height=42, variant="ghost"
        ).pack(fill="x", pady=4)

        RoundedButton(
            actions, text="Edit Profile", icon="✏",
            command=self.edit_profile, width=self.action_width, height=42
        ).pack(fill="x", pady=4)

        RoundedButton(
            actions, text="Delete Account", icon="🗑",
            command=self.delete_account, width=self.action_width, height=42, variant="danger"
        ).pack(fill="x", pady=4)

        RoundedButton(
            actions, text="Logout", icon="🚪",
            command=self.logout, width=self.action_width, height=42, variant="ghost"
        ).pack(fill="x", pady=4)

        # -----------------------------
        # Status Bar
        # -----------------------------
        self.status = tk.Label(
            self.frame,
            text="Ready",
            bg=theme.SURFACE,
            fg=theme.TEXT_FAINT,
            anchor="w",
            font=theme.FONT_SMALL,
            padx=10, pady=6
        )

        self.status.pack(side="bottom", fill="x", pady=(18, 0))

        self.refresh()

    # =====================================================
    def _make_info_row(self, parent, label_text):

        row = tk.Frame(parent, bg=theme.SURFACE)
        row.pack(fill="x", pady=3)

        tk.Label(
            row, text=label_text, bg=theme.SURFACE,
            fg=theme.TEXT_MUTED, font=theme.FONT_LABEL, width=10, anchor="w"
        ).pack(side="left")

        value = tk.Label(
            row, text="—", bg=theme.SURFACE,
            fg=theme.TEXT, font=theme.FONT_MONO, anchor="w"
        )
        value.pack(side="left", fill="x", expand=True)

        return value

    # =====================================================
    # Refresh Profile
    # =====================================================

    def refresh(self):

        response = api.get_me()

        if response.status_code != 200:

            try:
                detail = response.json()["detail"]
            except Exception:
                detail = response.text

            self.status.config(text=f"Error: {detail}", fg=theme.DANGER)
            self.status_dot.set_color(theme.DANGER)

            messagebox.showerror(
                "Error",
                detail
            )

            return

        user = response.json()

        self.title.config(
            text=f"Welcome, {user['username']}"
        )

        self.avatar.set_initials(user["username"])

        self.id_label.config(text=str(user["id"]))
        self.username_label.config(text=user["username"])
        self.email_label.config(text=user["email"])

        self.status_dot.set_color(theme.TEAL)

        self.status.config(
            text="Profile loaded successfully.",
            fg=theme.TEXT_FAINT
        )

    # =====================================================
    # Edit Profile
    # =====================================================

    def edit_profile(self):

        from profile_window import ProfileWindow

        ProfileWindow(
            self.root,
            refresh_callback=self.refresh
        )

    # =====================================================
    # Delete Account
    # =====================================================

    def delete_account(self):

        confirm = messagebox.askyesno(
            "Delete Account",
            "Deleting your account is permanent.\n\nDo you really want to continue?"
        )

        if not confirm:
            return

        response = api.delete_account()

        if response.status_code == 200:

            messagebox.showinfo(
                "Success",
                "Account deleted successfully."
            )

            config.TOKEN = None

            self.root.destroy()

        else:

            try:
                detail = response.json()["detail"]
            except Exception:
                detail = response.text

            messagebox.showerror(
                "Error",
                detail
            )

    # =====================================================
    # Logout
    # =====================================================

    def logout(self):

        confirm = messagebox.askyesno(
            "Logout",
            "Do you want to logout?"
        )

        if not confirm:
            return

        config.TOKEN = None

        self.root.destroy()
