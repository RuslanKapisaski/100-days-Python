from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

bricks = []

colors = ["red", "orange", "yellow", "green", "blue"]

for row in range(5):
    for col in range(10):
        brick = Brick(
            x=-360 + col * 80,
            y=250 - row * 30,
            color=colors[row]
        )
        bricks.append(brick)

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(paddle) < 70 and ball.ycor() < -230:
        ball.bounce_y()

    for brick in bricks:
        if ball.distance(brick) < 40:
            brick.hideturtle()
            bricks.remove(brick)
            ball.bounce_y()
            scoreboard.increase_score()
            break

    if ball.ycor() < -300:
        scoreboard.game_over()
        game_is_on = False

    if len(bricks) == 0:
        scoreboard.you_win()
        game_is_on = False

screen.exitonclick()