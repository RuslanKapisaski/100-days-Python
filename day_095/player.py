from turtle import Turtle

MOVE_DISTANCE = 20

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("cyan")
        self.penup()
        self.setheading(90)
        self.goto(0, -250)

    def move_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())