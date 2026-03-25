from turtle import Turtle,Screen
from random import randint

screen = Screen()
screen.setup(width=500,height=400)

is_race_on = False

colors = ['red','green','blue','yellow','orange','purple']

turtles=[]

for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    turtles.append(t)

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? ")

high_margin = 0

for turtle in turtles:
    turtle.penup()
    turtle.goto(-230,-100 + high_margin)
    high_margin += 66
    turtle.pendown()

if user_bet:
    is_race_on = True

winner = ""
while is_race_on:
    for turtle in turtles:
        random_move = randint(0,10)
        turtle.forward(random_move)
        if turtle.xcor() > 250:
            winner = turtle
            is_race_on = False

if user_bet != winner.color:
    print(f"You lose! Winner is the {winner.pencolor()} turtle!")
elif user_bet == winner.color:
    print(f"You win! Winner is the {winner.pencolor()} turtle!")


screen.exitonclick()