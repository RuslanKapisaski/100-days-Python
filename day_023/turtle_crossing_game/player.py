from turtle import Turtle

INITIAL_COORDINATES = (0,-280)

DIRECTION = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(INITIAL_COORDINATES)
        self.setheading(DIRECTION)
        self.y_move=10


    def move_up(self):
        new_y = self.ycor() + self.y_move
        self.goto(x=0,y=new_y)

    def is_at_finishline(self):
        if self.ycor()<-280:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(INITIAL_COORDINATES)


