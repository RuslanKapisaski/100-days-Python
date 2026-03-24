from random import choice
import colorgram
from turtle import Turtle, Screen

# You can try it also with different picture
colors = colorgram.extract('cat-picture.jpg', 10)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))
print(rgb_colors)

turtle = Turtle()
turtle.speed(0)
turtle.penup()

screen = Screen()
screen.colormode(255)

turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)

def draw_painting():
    turtle.dot(20, choice(rgb_colors))
    turtle.penup()
    turtle.forward(50)

for row in range(10):
    for _ in range(10):
        draw_painting()
    turtle.backward(500)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)

screen.exitonclick()