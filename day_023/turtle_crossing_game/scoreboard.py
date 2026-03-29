from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"

class Scoreboard:
    def __init__(self):
        self.scoreboard = Turtle()
        self.color="black"
        self.score = 0
        self.level = 1
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(-245,260)
        self.update_stats()

    def update_stats(self):
        self.scoreboard.clear()
        self.scoreboard.write(arg=f"Level: {self.level}\nScore: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_stats()

    def increase_level(self):
        self.level += 1
        self.update_stats()

    def game_over(self):
        self.scoreboard.clear()
        self.scoreboard.goto(x=0,y=0)
        self.scoreboard.write("Game Over",align=ALIGNMENT,font=FONT)