"""
Reusable, hand-drawn (canvas-based) widgets for the dark vault theme.

Kept separate from the individual window files so login_window,
dashboard and profile_window can all share the same controls:

- Card          : flat dark panel with a hairline border
- RoundedButton : rounded, hover-aware button drawn on a canvas
- FieldEntry    : labeled input with optional show/hide toggle
- VaultMark     : decorative padlock / keyhole mark (app signature)
- Avatar        : circular initials avatar
- StatusDot     : small colored status indicator
"""

import tkinter as tk

import theme


def _round_rect_points(x1, y1, x2, y2, r):
    r = min(r, (x2 - x1) / 2, (y2 - y1) / 2)
    return [
        x1 + r, y1,
        x2 - r, y1,
        x2, y1,
        x2, y1 + r,
        x2, y2 - r,
        x2, y2,
        x2 - r, y2,
        x1 + r, y2,
        x1, y2,
        x1, y2 - r,
        x1, y1 + r,
        x1, y1,
    ]


def _parent_bg(parent, fallback):
    try:
        return parent["bg"]
    except Exception:
        return fallback


class Card(tk.Frame):
    """A flat dark 'card' panel with a hairline border."""

    def __init__(self, parent, padding=20, **kwargs):
        super().__init__(
            parent,
            bg=theme.SURFACE,
            highlightbackground=theme.BORDER,
            highlightthickness=1,
            bd=0,
            **kwargs
        )
        self.inner = tk.Frame(self, bg=theme.SURFACE)
        self.inner.pack(fill="both", expand=True, padx=padding, pady=padding)


class RoundedButton(tk.Canvas):
    """A rounded, hover-aware button drawn on a canvas."""

    VARIANTS = {
        "primary": (theme.ACCENT, theme.ACCENT_HOVER),
        "danger": (theme.DANGER, theme.DANGER_HOVER),
        "ghost": (theme.SURFACE_ALT, theme.BORDER),
    }

    def __init__(self, parent, text, command=None, width=220, height=40,
                 variant="primary", icon="", radius=10):

        super().__init__(
            parent,
            width=width,
            height=height,
            bg=_parent_bg(parent, theme.SURFACE),
            highlightthickness=0,
            cursor="hand2"
        )

        self.command = command
        self.variant = variant
        self.radius = radius
        self.text = f"{icon}  {text}".strip() if icon else text
        self.width = width
        self.height = height
        self._enabled = True

        self._draw(self.VARIANTS[variant][0])

        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_click)

    def _draw(self, fill):
        self.delete("all")

        if self.variant == "ghost":
            text_color = theme.TEXT
            outline = theme.BORDER
        elif self.variant == "danger":
            text_color = "#FFFFFF"
            outline = fill
        else:
            text_color = "#12151C"
            outline = fill

        self.create_polygon(
            _round_rect_points(2, 2, self.width - 2, self.height - 2, self.radius),
            smooth=True,
            fill=fill,
            outline=outline
        )
        self.create_text(
            self.width / 2,
            self.height / 2,
            text=self.text,
            fill=text_color,
            font=theme.FONT_BUTTON
        )

    def _on_enter(self, _event):
        if self._enabled:
            self._draw(self.VARIANTS[self.variant][1])

    def _on_leave(self, _event):
        if self._enabled:
            self._draw(self.VARIANTS[self.variant][0])

    def _on_click(self, _event):
        if self._enabled and self.command:
            self.command()

    def set_enabled(self, enabled):
        self._enabled = enabled
        self.configure(cursor="hand2" if enabled else "arrow")
        fill_color = self.VARIANTS[self.variant][0] if enabled else theme.SURFACE_ALT
        self._draw(fill_color)


class FieldEntry(tk.Frame):
    """A labeled input field styled for the dark card layout,
    with an optional show/hide toggle for passwords."""

    def __init__(self, parent, label, icon="", show=None, width=30):
        super().__init__(parent, bg=_parent_bg(parent, theme.SURFACE))

        bg = _parent_bg(parent, theme.SURFACE)

        tk.Label(
            self,
            text=f"{icon}  {label}".strip(),
            bg=bg,
            fg=theme.TEXT_MUTED,
            font=theme.FONT_LABEL
        ).pack(anchor="w")

        self.entry_row = tk.Frame(
            self,
            bg=theme.SURFACE_ALT,
            highlightbackground=theme.BORDER,
            highlightthickness=1
        )
        self.entry_row.pack(fill="x", pady=(4, 0))

        self._show_char = show
        self.entry = tk.Entry(
            self.entry_row,
            font=theme.FONT_BODY,
            bg=theme.SURFACE_ALT,
            fg=theme.TEXT,
            insertbackground=theme.TEXT,
            relief="flat",
            show=show or "",
            width=width
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=(10, 4), pady=8)

        if show is not None:
            self._visible = False
            self.toggle = tk.Label(
                self.entry_row,
                text="Show",
                bg=theme.SURFACE_ALT,
                fg=theme.TEXT_FAINT,
                cursor="hand2",
                font=theme.FONT_SMALL
            )
            self.toggle.pack(side="right", padx=8)
            self.toggle.bind("<Button-1>", self._toggle_visibility)

        self.entry.bind("<FocusIn>", self._on_focus_in)
        self.entry.bind("<FocusOut>", self._on_focus_out)

    def _on_focus_in(self, _event):
        self.entry_row.configure(highlightbackground=theme.ACCENT)

    def _on_focus_out(self, _event):
        self.entry_row.configure(highlightbackground=theme.BORDER)

    def _toggle_visibility(self, _event):
        self._visible = not self._visible
        self.entry.configure(show="" if self._visible else self._show_char)
        self.toggle.configure(
            text="Hide" if self._visible else "Show",
            fg=theme.ACCENT if self._visible else theme.TEXT_FAINT
        )

    def get(self):
        return self.entry.get()

    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

    def clear(self):
        self.entry.delete(0, tk.END)


class VaultMark(tk.Canvas):
    """Decorative padlock / keyhole mark - the app's signature element."""

    def __init__(self, parent, size=64):
        super().__init__(
            parent,
            width=size,
            height=size,
            bg=_parent_bg(parent, theme.BG),
            highlightthickness=0
        )
        s = size
        cx = s / 2

        # shackle
        self.create_arc(
            s * 0.28, s * 0.05, s * 0.72, s * 0.55,
            start=0, extent=180,
            style="arc",
            outline=theme.ACCENT,
            width=max(2, s * 0.06)
        )

        # body
        self.create_polygon(
            _round_rect_points(s * 0.18, s * 0.42, s * 0.82, s * 0.92, s * 0.1),
            smooth=True,
            fill=theme.ACCENT,
            outline=""
        )

        # keyhole
        self.create_oval(
            cx - s * 0.06, s * 0.58, cx + s * 0.06, s * 0.70,
            fill=self["bg"], outline=""
        )
        self.create_polygon(
            cx - s * 0.035, s * 0.66,
            cx + s * 0.035, s * 0.66,
            cx + s * 0.05, s * 0.80,
            cx - s * 0.05, s * 0.80,
            fill=self["bg"], outline=""
        )


class Avatar(tk.Canvas):
    """Circular avatar showing a user's initial(s)."""

    def __init__(self, parent, initials="?", size=64):
        super().__init__(
            parent,
            width=size,
            height=size,
            bg=_parent_bg(parent, theme.SURFACE),
            highlightthickness=0
        )
        self.size = size
        self._paint(initials)

    def _paint(self, initials):
        self.delete("all")
        self.create_oval(
            2, 2, self.size - 2, self.size - 2,
            fill=theme.SURFACE_ALT,
            outline=theme.ACCENT,
            width=2
        )
        self.create_text(
            self.size / 2, self.size / 2,
            text=(initials or "?")[:2].upper(),
            fill=theme.ACCENT,
            font=("Segoe UI", int(self.size * 0.32), "bold")
        )

    def set_initials(self, initials):
        self._paint(initials)


class StatusDot(tk.Canvas):
    """Small colored status indicator dot."""

    def __init__(self, parent, color=None, size=10):
        color = color or theme.TEAL
        super().__init__(
            parent,
            width=size + 8,
            height=size + 8,
            bg=_parent_bg(parent, theme.SURFACE),
            highlightthickness=0
        )
        self.size = size
        self.set_color(color)

    def set_color(self, color):
        self.delete("all")
        pad = 4
        self.create_oval(pad, pad, pad + self.size, pad + self.size, fill=color, outline="")
