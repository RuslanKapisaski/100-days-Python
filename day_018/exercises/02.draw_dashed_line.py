from turtle import Turtle, Screen

# Draw a dashed line with the turtle

franklin = Turtle()

franklin.shape("turtle")

for _ in range(15):
    franklin.forward(10)
    franklin.penup()
    franklin.forward(10)
    franklin.pendown()


my_screen = Screen()
my_screen.exitonclick()