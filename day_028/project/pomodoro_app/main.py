from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text,text="00:00",fill="white",font=(FONT_NAME,40,"bold"))
    timer_label.config(text="Timer", fg=GREEN)
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global REPS

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if REPS % 2:
        count_down(short_break_seconds)
        timer_label.config(text="Short Break", fg=RED)
    elif REPS % 8:
        count_down(long_break_seconds)
        timer_label.config(text="Long Break", fg=PINK)
    else:
        count_down(work_seconds)
        timer_label.config(text="Work", fg=GREEN)

    REPS += 1

def count_down(count):
    global TIMER
    count_min = math.floor(count/60)
    count_sec = math.floor(count%60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
       TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = " "
        working_sessions = math.floot(REPS/2)
        for _ in range(working_sessions):
            mark = '✓'
            check_marks_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=223,bg=YELLOW,highlightthickness=0)
image = PhotoImage(file = "tomato.png")
canvas.create_image(103, 112, image=image)
timer_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,40,"bold"))
canvas.grid(row=1,column=1)


# Labels
timer_label = Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW,)
timer_label.grid(row=0,column=1)
check_marks_label = Label(text="", font=(FONT_NAME, 25), fg=GREEN, bg=YELLOW)
check_marks_label.grid(row=2, column=1)

# Buttons
start_btn = Button(text="Start", bg=YELLOW, activebackground=YELLOW, borderwidth=0,padx=10, pady=4,command=start_timer)
start_btn.grid(row=3,column=1)
start_btn.grid(row=2, column=0)
reset_btn = Button(text="Reset", bg=YELLOW, activebackground=YELLOW, borderwidth=0,padx=10, pady=4, command=reset_timer)
reset_btn.grid(row=2, column=2)


window.mainloop()