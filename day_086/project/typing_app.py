import tkinter as tk
from tkinter import font as tkfont
import os
import json
import random
import time
from .sample_texts import SAMPLE_TEXTS
from .score_helpers import save_score, load_scores

_THEME_FILE = os.path.join(os.path.dirname(__file__), "theme.json")
with open(_THEME_FILE) as _f:
    _c = json.load(_f)["COLORS"]

class TypingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("⌨  Typing Speed Test")
        self.configure(bg=_c["BG"])
        self.resizable(False, False)

        # State
        self.sample      = None
        self.start_time  = None
        self.timer_id    = None
        self.elapsed     = 0
        self.finished    = False
        self.test_active = False

        self._setup_fonts()
        self._build_ui()
        self._load_new_sample()
        self.after(100, self._center_window)

    # ── fonts ────────────────────────────────────────────────────────────────
    def _setup_fonts(self):
        self.f_mono_lg = tkfont.Font(family="Courier New", size=15)
        self.f_mono_sm = tkfont.Font(family="Courier New", size=12)
        self.f_sans_lg = tkfont.Font(family="Helvetica", size=22, weight="bold")
        self.f_sans_md = tkfont.Font(family="Helvetica", size=14, weight="bold")
        self.f_sans_sm = tkfont.Font(family="Helvetica", size=11)
        self.f_num     = tkfont.Font(family="Courier New", size=32, weight="bold")

    # ── layout ───────────────────────────────────────────────────────────────
    def _build_ui(self):
        root = tk.Frame(self, bg=_c["BG"], padx=32, pady=24)
        root.pack(fill="both", expand=True)

        # Header
        hdr = tk.Frame(root, bg=_c["BG"])
        hdr.pack(fill="x", pady=(0, 18))
        tk.Label(hdr, text="⌨  TYPING SPEED TEST", font=self.f_sans_lg,
                 bg=_c["BG"], fg=_c["ACCENT"]).pack(side="left")
        tk.Button(hdr, text="🏆 High Scores", font=self.f_sans_sm,
                  bg=_c["SURFACE2"], fg=_c["TEXT"], bd=0, padx=12, pady=6,
                  activebackground=_c["ACCENT"], activeforeground=_c["TEXT_BRIGHT"],
                  cursor="hand2", command=self._show_scores).pack(side="right")

        # Stats row
        stats = tk.Frame(root, bg=_c["BG"])
        stats.pack(fill="x", pady=(0, 14))
        self.wpm_var  = tk.StringVar(value="0")
        self.acc_var  = tk.StringVar(value="100")
        self.time_var = tk.StringVar(value="0")

        for label, var, unit, col in [
            ("WPM",      self.wpm_var,  "words/min", _c["ACCENT"]),
            ("ACCURACY", self.acc_var,  "%",          _c["GREEN"]),
            ("TIME",     self.time_var, "sec",        _c["YELLOW"]),
        ]:
            box = tk.Frame(stats, bg=_c["SURFACE"], bd=0, padx=20, pady=10)
            box.pack(side="left", expand=True, fill="x", padx=(0, 8))
            tk.Label(box, textvariable=var, font=self.f_num,
                     bg=_c["SURFACE"], fg=col).pack()
            tk.Label(box, text=f"{label}  ({unit})", font=self.f_sans_sm,
                     bg=_c["SURFACE"], fg=_c["TEXT_DIM"]).pack()

        # Category label
        self.category_var = tk.StringVar(value="")
        tk.Label(root, textvariable=self.category_var, font=self.f_sans_sm,
                 bg=_c["BG"], fg=_c["TEXT_DIM"]).pack(anchor="w", pady=(0, 6))

        # Sample text display
        sample_frame = tk.Frame(root, bg=_c["SURFACE2"], bd=0, padx=16, pady=14)
        sample_frame.pack(fill="x", pady=(0, 12))

        self.sample_text = tk.Text(
            sample_frame, font=self.f_mono_lg,
            bg=_c["SURFACE2"], fg=_c["TEXT_DIM"],
            wrap="word", height=5,
            bd=0, relief="flat",
            state="disabled", cursor="arrow",
            selectbackground=_c["SURFACE2"], selectforeground=_c["TEXT_DIM"],
        )
        self.sample_text.pack(fill="x")
        self.sample_text.tag_config("correct",   foreground=_c["TEXT_BRIGHT"])
        self.sample_text.tag_config("incorrect",  foreground=_c["RED"], background="#2a1a1a")
        self.sample_text.tag_config("cursor_pos", foreground=_c["BG"],       background=_c["ACCENT"])
        self.sample_text.tag_config("ahead",      foreground=_c["TEXT_DIM"])

        # Input area
        input_frame = tk.Frame(root, bg=_c["SURFACE"], bd=0, padx=14, pady=10)
        input_frame.pack(fill="x", pady=(0, 14))
        tk.Label(input_frame, text="Type here →", font=self.f_sans_sm,
                 bg=_c["SURFACE"], fg=_c["TEXT_DIM"]).pack(anchor="w")
        self.input_var = tk.StringVar()
        self.input_var.trace_add("write", self._on_type)
        self.entry = tk.Entry(
            input_frame, textvariable=self.input_var,
            font=self.f_mono_lg,
            bg=_c["SURFACE2"], fg=_c["TEXT_BRIGHT"],
            insertbackground=_c["CURSOR_COL"],
            bd=0, relief="flat", justify="left",
        )
        self.entry.pack(fill="x", pady=(4, 0), ipady=6)
        self.entry.bind("<Return>", lambda e: self._restart())
        self.entry.bind("<FocusIn>", self._on_focus)

        # Buttons
        btn_row = tk.Frame(root, bg=_c["BG"])
        btn_row.pack(fill="x")
        self.btn_restart = tk.Button(
            btn_row, text="↺  New Test", font=self.f_sans_md,
            bg=_c["ACCENT"], fg=_c["TEXT_BRIGHT"], bd=0, padx=20, pady=8,
            activebackground="#5a4bcc", activeforeground=_c["TEXT_BRIGHT"],
            cursor="hand2", command=self._restart,
        )
        self.btn_restart.pack(side="left", padx=(0, 10))

        self.btn_shuffle = tk.Button(
            btn_row, text="⇄  Different Text", font=self.f_sans_sm,
            bg=_c["SURFACE2"], fg=_c["TEXT"], bd=0, padx=16, pady=8,
            activebackground=_c["SURFACE"], activeforeground=_c["TEXT_BRIGHT"],
            cursor="hand2", command=self._shuffle,
        )
        self.btn_shuffle.pack(side="left")

        # Result banner (hidden initially)
        self.result_frame = tk.Frame(root, bg=_c["SURFACE2"], padx=20, pady=14)
        self.result_label = tk.Label(
            self.result_frame, text="", font=self.f_sans_md,
            bg=_c["SURFACE2"], fg=_c["GREEN"], wraplength=560, justify="center",
        )
        self.result_label.pack()

        # Progress bar
        pb_frame = tk.Frame(root, bg=_c["SURFACE2"], height=6)
        pb_frame.pack(fill="x", pady=(14, 0))
        self.progress_bar = tk.Frame(pb_frame, bg=_c["ACCENT"], height=6)
        self.progress_bar.place(x=0, y=0, relheight=1.0, relwidth=0.0)
        self._pb_width = 0   # 0–1 float

    # ── helpers ──────────────────────────────────────────────────────────────
    def _center_window(self):
        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"+{(sw-w)//2}+{(sh-h)//2}")

    def _load_new_sample(self, sample=None):
        self.sample = sample or random.choice(SAMPLE_TEXTS)
        self.category_var.set(f"📂  {self.sample['title']}")
        self._render_sample("", "")

    def _render_sample(self, typed: str, target: str):
        """Colour-annotate the sample text based on what was typed."""
        self.sample_text.config(state="normal")
        self.sample_text.delete("1.0", "end")
        full = self.sample["text"]
        i = 0
        for i, ch in enumerate(typed):
            if i >= len(full):
                break
            tag = "correct" if ch == full[i] else "incorrect"
            self.sample_text.insert("end", full[i], tag)
        # cursor position character
        if i + 1 <= len(full) and typed:
            pos = len(typed)
            if pos < len(full):
                self.sample_text.insert("end", full[pos], "cursor_pos")
                self.sample_text.insert("end", full[pos+1:], "ahead")
            else:
                pass   # finished
        elif not typed:
            if full:
                self.sample_text.insert("end", full[0], "cursor_pos")
                self.sample_text.insert("end", full[1:], "ahead")
        self.sample_text.config(state="disabled")

        # progress bar
        frac = min(len(typed) / max(len(full), 1), 1.0)
        self.progress_bar.place(relwidth=frac)

    def _start_timer(self):
        self.start_time = time.time()
        self.test_active = True
        self._tick()

    def _tick(self):
        if not self.test_active:
            return
        self.elapsed = time.time() - self.start_time
        self.time_var.set(str(int(self.elapsed)))
        # live WPM
        typed = self.input_var.get()
        words_typed = len(typed.split())
        wpm = (words_typed / self.elapsed * 60) if self.elapsed > 0 else 0
        self.wpm_var.set(str(int(wpm)))
        self.timer_id = self.after(500, self._tick)

    def _compute_accuracy(self, typed: str) -> float:
        target = self.sample["text"][:len(typed)]
        if not typed:
            return 100.0
        correct = sum(a == b for a, b in zip(typed, target))
        return correct / len(typed) * 100

    def _on_type(self, *_):
        typed = self.input_var.get()

        # Start timer on first keypress
        if not self.test_active and typed:
            self._start_timer()

        target = self.sample["text"]
        self._render_sample(typed, target)

        # Update accuracy
        acc = self._compute_accuracy(typed)
        self.acc_var.set(str(int(acc)))

        # Colour entry border by accuracy
        self.entry.config(fg=_c["TEXT_BRIGHT"] if acc >= 90 else _c["YELLOW"] if acc >= 75 else _c["RED"])

        # Finished?
        if len(typed) >= len(target) and not self.finished:
            self._finish(typed)

    def _finish(self, typed: str):
        self.finished = True
        self.test_active = False
        if self.timer_id:
            self.after_cancel(self.timer_id)

        elapsed = time.time() - self.start_time
        word_count = len(self.sample["text"].split())
        wpm = word_count / elapsed * 60
        acc = self._compute_accuracy(typed)

        self.wpm_var.set(str(int(wpm)))
        self.acc_var.set(str(int(acc)))
        self.time_var.set(str(int(elapsed)))

        # Rating
        if wpm >= 100:   rating, col = "🚀 Expert typist!", _c["ACCENT"]
        elif wpm >= 70:  rating, col = "🔥 Advanced typist!", _c["GREEN"]
        elif wpm >= 55:  rating, col = "✅ Above average!", _c["GREEN"]
        elif wpm >= 40:  rating, col = "👍 Average speed.", _c["YELLOW"]
        else:            rating, col = "📘 Keep practising!", _c["RED"]

        self.result_label.config(
            text=f"{rating}   {wpm:.1f} WPM  ·  {acc:.0f}% accuracy  ·  {elapsed:.1f}s\n"
                 f"(Press Enter or click ↺ New Test to go again)",
            fg=col,
        )
        self.result_frame.pack(fill="x", pady=(14, 0))

        save_score(wpm, acc, self.sample["title"])
        self.entry.config(state="disabled")

    def _on_focus(self, _):
        if not self.test_active and not self.finished:
            pass   # ready to start

    def _restart(self):
        """Reset with the same text."""
        self._cancel_timer()
        self.finished    = False
        self.test_active = False
        self.elapsed     = 0
        self.input_var.set("")
        self.wpm_var.set("0")
        self.acc_var.set("100")
        self.time_var.set("0")
        self.entry.config(state="normal", fg=_c["TEXT_BRIGHT"])
        self.result_frame.pack_forget()
        self._render_sample("", "")
        self.entry.focus_set()

    def _shuffle(self):
        """Reset with a new random text (different from current)."""
        current = self.sample
        new = random.choice([s for s in SAMPLE_TEXTS if s is not current])
        self._cancel_timer()
        self.finished    = False
        self.test_active = False
        self.elapsed     = 0
        self.input_var.set("")
        self.wpm_var.set("0")
        self.acc_var.set("100")
        self.time_var.set("0")
        self.entry.config(state="normal", fg=_c["TEXT_BRIGHT"])
        self.result_frame.pack_forget()
        self._load_new_sample(new)
        self.entry.focus_set()

    def _cancel_timer(self):
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None

    # ── high-score window ────────────────────────────────────────────────────
    def _show_scores(self):
        scores = load_scores()
        win = tk.Toplevel(self)
        win.title("🏆 High Scores")
        win.configure(bg=_c["BG"])
        win.resizable(False, False)

        tk.Label(win, text="🏆  TOP 10 SCORES", font=self.f_sans_md,
                 bg=_c["BG"], fg=_c["ACCENT"], pady=16).pack()

        frame = tk.Frame(win, bg=_c["SURFACE"], padx=24, pady=16)
        frame.pack(padx=24, pady=(0, 16))

        if not scores:
            tk.Label(frame, text="No scores yet — complete a test!",
                     font=self.f_sans_sm, bg=_c["SURFACE"], fg=_c["TEXT_DIM"]).pack()
        else:
            headers = ["#", "WPM", "Accuracy", "Category"]
            for col, h in enumerate(headers):
                tk.Label(frame, text=h, font=self.f_sans_sm,
                         bg=_c["SURFACE"], fg=_c["TEXT_DIM"], padx=12).grid(row=0, column=col, sticky="w")
            for i, s in enumerate(scores, 1):
                medal = ["🥇","🥈","🥉"].get(i-1, f"{i} ") if i <= 3 else f"{i}."
                col_wpm = _c["GREEN"] if s["wpm"] >= 70 else _c["YELLOW"] if s["wpm"] >= 40 else _c["RED"]
                for col, (val, fg) in enumerate([
                    (medal,             _c["TEXT_DIM"]),
                    (f"{s['wpm']}",     col_wpm),
                    (f"{s['accuracy']}%", _c["TEXT"]),
                    (s["title"],        _c["TEXT_DIM"]),
                ]):
                    tk.Label(frame, text=val, font=self.f_mono_sm,
                             bg=_c["SURFACE"], fg=fg, padx=12, pady=3).grid(row=i, column=col, sticky="w")

        tk.Button(win, text="Close", font=self.f_sans_sm,
                  bg=_c["SURFACE2"], fg=_c["TEXT"], bd=0, padx=16, pady=6,
                  command=win.destroy, cursor="hand2").pack(pady=(0, 16))

        win.update_idletasks()
        x = self.winfo_x() + (self.winfo_width()  - win.winfo_width())  // 2
        y = self.winfo_y() + (self.winfo_height() - win.winfo_height()) // 2
        win.geometry(f"+{x}+{y}")

