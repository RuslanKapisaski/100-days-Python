from turtle import Turtle

class Enemy(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(x, y)