import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk
import os

from .positions import POSITIONS
from .watermark import add_watermark

class App(tk.Tk):
    BG = "#f5f4f0"
    PANEL = "#ffffff"
    BORDER = "#e0ddd6"
    TEXT = "#1a1a1a"
    MUTED = "#888880"
    ACCENT = "#1a1a1a"

    def __init__(self):
        super().__init__()
        self.title("Watermark Tool")
        self.configure(bg=self.BG)
        self.resizable(False, False)

        # state
        self.image_path = ""
        self.source_img = None
        self.preview_tk = None
        self.wm_text = tk.StringVar(value="© yourwebsite.com")
        self.font_size = tk.IntVar(value=38)
        self.opacity = tk.IntVar(value=70)
        self.position = tk.StringVar(value="Bottom-Right")
        self.color = "#ffffff"

        self._build()

    # ── UI ──────────────────────────────────────────────────────────────────────

    def _build(self):
        # left panel ─ controls
        left = tk.Frame(self, bg=self.PANEL, width=280)
        left.pack(side="left", fill="y")
        left.pack_propagate(False)

        # right panel ─ preview
        right = tk.Frame(self, bg=self.BG)
        right.pack(side="left", fill="both", expand=True)

        self._build_controls(left)
        self._build_preview(right)

    def _build_controls(self, p):
        pad = dict(padx=20, pady=0)

        # title
        tk.Label(p, text="Watermark", font=("Georgia", 18, "italic"),
                 bg=self.PANEL, fg=self.TEXT).pack(anchor="w", padx=20, pady=(24, 2))
        tk.Label(p, text="Tool", font=("Georgia", 18),
                 bg=self.PANEL, fg=self.TEXT).pack(anchor="w", padx=20, pady=(0, 20))

        self._divider(p)

        # open image
        self._label(p, "Image")
        self._btn(p, "Open image…", self._open_image)
        self.img_label = tk.Label(p, text="No image selected",
                                  font=("Courier", 8), bg=self.PANEL,
                                  fg=self.MUTED, wraplength=240, justify="left")
        self.img_label.pack(anchor="w", **pad)

        self._divider(p)

        # text
        self._label(p, "Watermark text")
        tk.Entry(p, textvariable=self.wm_text,
                 font=("Courier", 11), bg=self.BG, fg=self.TEXT,
                 relief="flat", bd=0,
                 highlightthickness=1,
                 highlightbackground=self.BORDER,
                 highlightcolor=self.ACCENT
                 ).pack(fill="x", **pad, ipady=6)

        # font size
        self._label(p, "Size")
        self._slider(p, self.font_size, 12, 100)

        # opacity
        self._label(p, "Opacity")
        self._slider(p, self.opacity, 10, 100)

        # color
        self._label(p, "Colour")
        color_row = tk.Frame(p, bg=self.PANEL)
        color_row.pack(fill="x", **pad)
        self.swatch = tk.Frame(color_row, bg=self.color,
                               width=24, height=24, cursor="hand2")
        self.swatch.pack(side="left")
        self.swatch.bind("<Button-1>", self._pick_color)
        tk.Label(color_row, textvariable=tk.StringVar(value="  click to change"),
                 font=("Courier", 9), bg=self.PANEL, fg=self.MUTED
                 ).pack(side="left")

        # position
        self._label(p, "Position")
        pos_frame = tk.Frame(p, bg=self.PANEL)
        pos_frame.pack(fill="x", **pad)

        for pos in POSITIONS:
            tk.Radiobutton(pos_frame, text=pos, variable=self.position,
                           value=pos, bg=self.PANEL, fg=self.TEXT,
                           selectcolor=self.BG, activebackground=self.PANEL,
                           font=("Courier", 9), cursor="hand2",
                           command=self._preview
                           ).pack(anchor="w")

        self._divider(p)

        # save
        self._btn(p, "Save image", self._save, accent=True)
        tk.Label(p, text="day 085 · python + pillow",
                 font=("Courier", 8), bg=self.PANEL, fg=self.BORDER
                 ).pack(side="bottom", pady=12)

    def _build_preview(self, p):
        tk.Label(p, text="Preview", font=("Courier", 9),
                 bg=self.BG, fg=self.MUTED).pack(anchor="w", padx=20, pady=(20, 6))

        self.canvas = tk.Canvas(p, bg=self.BORDER, highlightthickness=0,
                                width=800, height=600)
        self.canvas.pack(padx=20, pady=(0, 20))

        self.hint = self.canvas.create_text(
            280, 210, text="Open an image to begin",
            font=("Georgia", 13, "italic"), fill="#aaa8a0")

        # live-update bindings
        self.wm_text.trace_add("write", lambda *_: self._preview())
        self.font_size.trace_add("write", lambda *_: self._preview())
        self.opacity.trace_add("write", lambda *_: self._preview())

    # ── helpers ──────────────────────────────────────────────────────────────────

    def _label(self, p, text):
        tk.Label(p, text=text.upper(), font=("Courier", 8),
                 bg=self.PANEL, fg=self.MUTED
                 ).pack(anchor="w", padx=20, pady=(10, 0))

    def _divider(self, p):
        tk.Frame(p, bg=self.BORDER, height=1).pack(fill="x", padx=20, pady=8)

    def _btn(self, p, text, cmd, accent=False):
        bg = self.ACCENT if accent else self.BG
        fg = "#ffffff" if accent else self.TEXT
        tk.Button(p, text=text, command=cmd,
                  bg=bg, fg=fg, activebackground=self.MUTED,
                  activeforeground="#fff", relief="flat", bd=0,
                  font=("Courier", 10), cursor="hand2", pady=9
                  ).pack(fill="x", padx=20, pady=(4, 0))

    def _slider(self, p, var, lo, hi):
        frm = tk.Frame(p, bg=self.PANEL)
        frm.pack(fill="x", padx=20, pady=(2, 8))

        val = tk.Label(
            frm,
            font=("Courier", 9),
            bg=self.PANEL,
            fg=self.TEXT,
            width=4,
            anchor="e",
        )
        val.pack(side="right")

        def _update(_=None):
            val.config(text=str(var.get()))

        tk.Scale(
            frm,
            from_=lo,
            to=hi,
            variable=var,
            orient="horizontal",
            bg=self.PANEL,
            fg=self.TEXT,
            troughcolor=self.BG,
            highlightthickness=0,
            showvalue=False,
            bd=0,
            command=_update,
        ).pack(side="left", fill="x", expand=True)

        _update()

    # ── actions ──────────────────────────────────────────────────────────────────

    def _open_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Images", "*.jpg *.jpeg *.png *.webp *.bmp"), ("All", "*.*")])
        if not path:
            return
        self.image_path = path
        self.source_img = Image.open(path)
        self.img_label.config(text=os.path.basename(path))
        self._preview()

    def _pick_color(self, _=None):
        result = colorchooser.askcolor(color=self.color, title="Watermark colour")
        if result and result[1]:
            self.color = result[1]
            self.swatch.config(bg=self.color)
            self._preview()

    def _preview(self):
        if not self.source_img:
            return
        result = add_watermark(
            self.source_img,
            self.wm_text.get(),
            self.font_size.get(),
            self.color,
            self.opacity.get(),
            self.position.get(),
        )
        result.thumbnail((560, 420), Image.LANCZOS)
        self.preview_tk = ImageTk.PhotoImage(result)
        self.canvas.delete("all")
        w, h = result.size
        self.canvas.config(width=max(w, 490), height=max(h, 560))
        self.canvas.create_image(max(w, 480) // 2, max(h, 420) // 2,
                                 image=self.preview_tk, anchor="center")

    def _save(self):
        if not self.source_img:
            messagebox.showwarning("No image", "Please open an image first.")
            return
        result = add_watermark(
            self.source_img,
            self.wm_text.get(),
            self.font_size.get(),
            self.color,
            self.opacity.get(),
            self.position.get(),
        )
        base, ext = os.path.splitext(self.image_path)
        out = filedialog.asksaveasfilename(
            initialfile=os.path.basename(base) + "_watermarked" + (ext or ".jpg"),
            defaultextension=ext or ".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("All", "*.*")],
        )
        if out:
            result.convert("RGB").save(out, quality=95)
            messagebox.showinfo("Saved", f"Saved to:\n{out}")
