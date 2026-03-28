from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score} | {self.r_score}", align='center', font=("Courier", 30, "bold"))

    def increase_l_score(self):
        self.l_score += 1
        self.update_score()

    def increase_r_score(self):
        self.r_score += 1
        self.update_score()

    def show_winner(self, message):
        self.clear()
        self.write(arg=message, align='center', font=("Arial", 18, "normal"))

    def reset_score(self):
        self.l_score = 0
        self.r_score = 0

