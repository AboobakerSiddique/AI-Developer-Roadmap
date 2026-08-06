"""
Dark 'Vault' theme for the Authentication System desktop app.

Design language: a secure digital vault - deep charcoal-navy surfaces,
a warm brass/gold accent (the "key"), and a teal accent for
success / active states. Rounded, hand-drawn controls (see windows.py)
replace the default flat ttk widgets so the app doesn't read as a
stock tkinter form.
"""

from tkinter import ttk

# ----------------------------------------------------------------
# Color tokens
# ----------------------------------------------------------------
BG = "#0B0E14"              # app background - near-black navy
SURFACE = "#151A24"         # card background
SURFACE_ALT = "#1C222E"     # inputs / hover / elevated surface
BORDER = "#2A3140"          # hairline borders

ACCENT = "#E8A94A"          # brass / gold - the "key"
ACCENT_HOVER = "#F2BB63"
ACCENT_DIM = "#8C6A32"

TEAL = "#2DD9C4"            # success / active status
DANGER = "#E8615D"          # errors / destructive actions
DANGER_HOVER = "#F27874"

TEXT = "#E8EAF0"
TEXT_MUTED = "#8891A5"
TEXT_FAINT = "#5A6376"

# ----------------------------------------------------------------
# Fonts
# ----------------------------------------------------------------
FONT_DISPLAY = ("Segoe UI", 21, "bold")
FONT_TITLE = ("Segoe UI", 13, "bold")
FONT_BODY = ("Segoe UI", 10)
FONT_LABEL = ("Segoe UI", 9)
FONT_SMALL = ("Segoe UI", 8)
FONT_MONO = ("Consolas", 9)
FONT_BUTTON = ("Segoe UI", 10, "bold")


def apply_theme(root):
    """Configure the root window + ttk styles for the dark vault theme."""

    root.configure(bg=BG)

    style = ttk.Style(root)

    try:
        style.theme_use("clam")
    except Exception:
        pass

    style.configure("TFrame", background=BG)
    style.configure("Card.TFrame", background=SURFACE)

    style.configure(
        "TLabel",
        background=BG,
        foreground=TEXT,
        font=FONT_BODY
    )

    style.configure(
        "TEntry",
        fieldbackground=SURFACE_ALT,
        background=SURFACE_ALT,
        foreground=TEXT,
        bordercolor=BORDER,
        insertcolor=TEXT,
        padding=8,
        relief="flat"
    )

    style.map(
        "TEntry",
        fieldbackground=[("focus", SURFACE_ALT)],
        bordercolor=[("focus", ACCENT)]
    )

    style.configure(
        "Vertical.TScrollbar",
        background=SURFACE,
        troughcolor=BG,
        bordercolor=BG,
        arrowcolor=TEXT_MUTED
    )

    return style
