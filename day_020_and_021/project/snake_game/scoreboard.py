from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard():
    def __init__(self):
        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.score = 0
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0,270)
        self.update_score()

    def update_score(self):
        self.scoreboard.write(arg=f"Score:{self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.scoreboard.score += 1
        self.scoreboard.clear()
        self.scoreboard.update_score()

    def game_over(self):
        self.scoreboard.clear()
        self.scoreboard.goto(0,0)
        self.scoreboard.write(f"GAME OVER!\nScore: {self.score}",align=ALIGNMENT,font=FONT)
