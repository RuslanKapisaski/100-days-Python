from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

# Game objects
ball = Ball()
r_paddle = Paddle(x_pos=350, y_pos=0)
l_paddle = Paddle(x_pos=-350, y_pos=0)
scoreboard = Scoreboard()

# Controls
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# Restart key
screen.onkey(lambda: restart_game(), "r")
screen.onkey(lambda: end_game(), "e")

# Boundaries
top_y_coordinates = 290
bottom_y_coordinates = -290

# Game state
game_speed = 0.02
game_is_on = True


def play_game():
    global game_is_on

    while game_is_on:
        time.sleep(game_speed)
        screen.update()
        ball.move()

        # Wall collision
        if ball.ycor() >= top_y_coordinates or ball.ycor() <= bottom_y_coordinates:
            ball.bounce_y()

        # Paddle collision
        if ball.distance(r_paddle) < 60 and ball.xcor() > 320:
            ball.bounce_x()

        if ball.distance(l_paddle) < 60 and ball.xcor() < -320:
            ball.bounce_x()

        # Scoring

        if ball.xcor() > 400:
            scoreboard.increase_l_score()
            ball.reset_position()

        if ball.xcor() < -400:
            scoreboard.increase_r_score()
            ball.reset_position()


def restart_game():
    global game_is_on

    game_is_on = True

    # Clear old message
    scoreboard.clear()
    scoreboard.reset_score()

    # Reset ball
    ball.goto(0, 0)
    ball.x_move = 10
    ball.y_move = 10

    play_game()


def end_game():
    global game_is_on
    game_is_on = False


# Start game
play_game()

screen.exitonclick()