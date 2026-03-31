import turtle
import pandas

df = pandas.read_csv("50_states.csv")
states = df.state
print(len(states))

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed = []
while len(guessed) < 50:
    guess = screen.textinput(title=f"{len(guessed)}/50 States Correct",
                             prompt="What's the next state?: ")

    if guess is None:
        print("Game exited by user.")
        break
    guess = guess.title().strip()

    for state in states:
        if state == guess:
            guessed.append(state)
            print(len(guessed))
            x = df[df["state"] == guess].iloc[0].x
            y = df[df["state"] == guess].iloc[0].y

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x, y)
            t.write(state)

missed = [state for state in states if state not in guessed]
missed_df = pandas.DataFrame({"Missed States": missed})
missed_df.to_csv("missed_states.csv", index=False)

turtle.mainloop()


