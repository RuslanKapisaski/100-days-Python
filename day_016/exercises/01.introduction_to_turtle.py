# Turtle Graphics
# Introduction
# Turtle graphics is an implementation of the popular geometric drawing tools introduced in Logo,
# developed by Wally Feurzeig, Seymour Papert and Cynthia Solomon in 1967.

#Move the turle forward by 100 paces

from turtle import Turtle, Screen

frank = Turtle()

frank.shape("turtle")
frank.color("green")
frank.forward(100)



my_screen = Screen()
my_screen.exitonclick()



