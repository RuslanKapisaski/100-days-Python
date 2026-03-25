from turtle import Turtle, Screen


franklin =Turtle()
franklin.shape("turtle")
screen = Screen()

def move_forwards():
    franklin.forward(20)

def move_backwards():
    franklin.backward(20)

def move_clockwise():
    franklin.right(90)

def move_counterclockwise():
    franklin.left(90)

def clear():
    franklin.clear()
    franklin.penup()
    franklin.home()
    franklin.pendown()

screen.listen()

screen.onkey(key= "w",fun = move_forwards)
screen.onkey(key= "s",fun = move_backwards)
screen.onkey(key= "d",fun = move_clockwise)
screen.onkey(key= "a",fun = move_counterclockwise)
screen.onkey(key= "c",fun = clear)

screen.exitonclick()