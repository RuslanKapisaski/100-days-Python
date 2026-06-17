from turtle import Turtle

MOVE_SPEED = 15

class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.2, stretch_len=0.8)
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.state = "ready"

    def fire(self, x, y):

        if self.state == "ready":
            self.state = "fire"
            self.goto(x, y + 15)
            self.showturtle()

    def move(self):

        if self.state == "fire":
            self.goto(
                self.xcor(),
                self.ycor() + MOVE_SPEED)

            if self.ycor() > 300:
                self.reset_bullet()

    def reset_bullet(self):
        self.hideturtle()
        self.state = "ready"
        self.goto(0, -400)