from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.goto(0, -260)

    def go_left(self):
        new_x = self.xcor() - 40
        if new_x > -330:
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 40
        if new_x < 330:
            self.goto(new_x, self.ycor())