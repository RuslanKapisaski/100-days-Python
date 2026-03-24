from turtle import Turtle, Screen
from random import randint

my_screen = Screen()
my_screen.colormode(255)

franklin = Turtle()
franklin.speed("fastest")
franklin.shape("turtle")
franklin.width(2)

rotation_degrees = 0

def randomize_color():
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    color = (red,green,blue)
    return  color

def draw_spirograph():
    franklin.left(6)
    franklin.circle(200)

while rotation_degrees <= 360:
    franklin.color(randomize_color())
    draw_spirograph()
    rotation_degrees += 6

my_screen.exitonclick()