import tkinter as tk

TIME_LIMIT = 5

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")
        self.root.geometry("700x500")

        self.time_left = TIME_LIMIT
        self.timer_running = False

        self.label = tk.Label(
            root,
            text="Keep writing! If you stop for 5 seconds, everything will be deleted.",
            font=("Arial", 14)
        )
        self.label.pack(pady=10)

        self.timer_label = tk.Label(root, text=f"Time left: {self.time_left}", font=("Arial", 16))
        self.timer_label.pack()

        self.text_area = tk.Text(root, font=("Arial", 14), wrap="word")
        self.text_area.pack(expand=True, fill="both", padx=20, pady=20)

        self.text_area.bind("<Key>", self.reset_timer)

        self.countdown()

    def reset_timer(self, event=None):
        self.time_left = TIME_LIMIT
        self.timer_label.config(text=f"Time left: {self.time_left}")

    def countdown(self):
        if self.text_area.get("1.0", tk.END).strip():
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}")

            if self.time_left <= 0:
                self.text_area.delete("1.0", tk.END)
                self.time_left = TIME_LIMIT
                self.timer_label.config(text="Text deleted!")

        self.root.after(1000, self.countdown)
