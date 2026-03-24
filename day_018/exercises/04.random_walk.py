import turtle
from turtle import Turtle, Screen
from random import choice, randint

turtle.colormode(255)

franklin = Turtle()
screen = Screen()

franklin.speed("fastest")
franklin.pensize(20)
franklin.width(3)
franklin.speed(3)


def randomize_color():
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)

    color = (red,green,blue)
    return  color

def random_walk():
    franklin.color(randomize_color())
    angles = [0,90,180,270]
    random_angle = choice(angles)
    franklin.setheading(random_angle)
    franklin.forward(10)

for _ in range(100):
    random_walk()

screen.exitonclick()