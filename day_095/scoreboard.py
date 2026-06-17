from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score}",
            align="center",
            font=("Arial", 18, "normal")
        )

    def increase_score(self):
        self.score += 10
        self.update_score()