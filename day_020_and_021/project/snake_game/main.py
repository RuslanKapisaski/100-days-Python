from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.title("Snake Game")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(key= "Up",fun = snake.up,)
screen.onkey(key= "Down",fun = snake.down)
screen.onkey(key= "Right",fun = snake.right)
screen.onkey(key= "Left",fun = snake.left)

game_speed = 0.2

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect wall collision (wrap-around)
    if snake.head.xcor() > 280:
        snake.head.goto(-280, snake.head.ycor())
    elif snake.head.xcor() < -280:
        snake.head.goto(280, snake.head.ycor())
    elif snake.head.ycor() > 280:
        snake.head.goto(snake.head.xcor(), -280)
    elif snake.head.ycor() < -280:
        snake.head.goto(snake.head.xcor(), 280)

    # Detect tail collision (separate block)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_on = False

screen.exitonclick()
