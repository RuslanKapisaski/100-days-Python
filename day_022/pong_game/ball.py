from turtle import Turtle
from random import choice

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x_pos = self.xcor() + self.x_move
        new_y_pos = self.ycor() + self.y_move
        self.penup()
        self.goto(new_x_pos,new_y_pos)

    def reset_position(self):
        new_x_pos = 0
        new_y_pos = choice([-250,250])
        self.goto(new_x_pos, new_y_pos)
        self.bounce_x()


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1