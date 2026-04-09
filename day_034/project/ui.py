from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quizz_brain):
        self.quiz = quizz_brain
        self.score = 0
        self.question_text = self.quiz.current_question

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=2)
        self.questions_count_label = Label(text=f"Question: {self.quiz.question_number} / {len(self.quiz.question_list)}", fg="white", bg=THEME_COLOR)
        self.questions_count_label.grid(row=0, column=0)

        self.canvas = Canvas(self.window, bg="white")
        self.canvas.config(width=300, height=250)
        self.question_item = self.canvas.create_text(
            150, 125,
            fill="black",
            font="Arial 20 italic",
            text="",
            width=280,
        )
        self.canvas.grid(row=1, column=0, columnspan=3)

        self.yes_img = PhotoImage(file="./images/true.png")
        self.no_img = PhotoImage(file="./images/false.png")

        self.no_btn = Button(image=self.no_img, bg=THEME_COLOR,highlightthickness=0,  command=lambda: self.check_answer("False"))
        self.no_btn.grid(row=2, column=0, pady=20)

        self.yes_btn = Button(image=self.yes_img, bg=THEME_COLOR,highlightthickness=0,command=lambda: self.check_answer("True"))
        self.yes_btn.grid(row=2, column=2, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def check_answer(self, answer):
        is_correct = self.quiz.check_answer(answer)
        if is_correct:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        self.get_next_question()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()

            self.questions_count_label.config(text=f"Question: {self.quiz.question_number} / {len(self.quiz.question_list)}")
            self.canvas.itemconfig(self.question_item, text=q_text)
            self.no_btn.config(state="normal")
            self.yes_btn.config(state="normal")
        else:
            self.canvas.itemconfig(self.question_item, text=f"You've completed the quiz!\nYour current score is: {self.score}/{self.quiz.question_number}")
            self.no_btn.config(state="disabled")
            self.yes_btn.config(state="disabled")

