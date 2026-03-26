from turtle import Screen,Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key= "Up",fun = snake.up,)
screen.onkey(key= "Down",fun = snake.down)
screen.onkey(key= "Right",fun = snake.right)
screen.onkey(key= "Left",fun = snake.left)

game_speed = 0.1
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()

screen.exitonclick()
