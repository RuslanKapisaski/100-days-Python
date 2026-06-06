"""
Day 086 — Typing Speed Test
A desktop typing trainer with WPM tracking, high scores, and multiple text samples.
Run with: python typing_speed_test.py
"""
from project.typing_app import TypingApp

# ── entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = TypingApp()
    app.mainloop()