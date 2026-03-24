from turtle import Turtle,Screen
from random import sample

turtle_colors = [
    "green",
    "olive",
    "darkgreen",
    "lightgreen",
    "brown",
    "saddlebrown",
    "tan",
    "khaki",
    "yellow",
    "gold",
    "orange",
    "darkolivegreen",
    "teal",
    "seagreen",
    "black"
]

franklin = Turtle()
franklin.shape("turtle")

scale = 1
num_sides = 3

def randomize_color(turtle_colors):
    return sample(turtle_colors, k=1)

def draw_shape(num_sides,scale):
    random_color = randomize_color(turtle_colors)
    franklin.color(random_color)
    for _ in range(num_sides):
        angle = 360 / num_sides
        franklin.forward(100*scale)
        franklin.right(angle)
    scale += 0.05

while num_sides < 10:
    draw_shape(num_sides,scale)
    num_sides+=1

screen = Screen()
screen.exitonclick()