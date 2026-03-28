from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x_pos,y_pos)

    def move_up(self):
        self.penup()
        self.sety(self.ycor() + 40)

    def move_down(self):
        self.penup()
        self.sety(self.ycor() - 40)
