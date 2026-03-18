import random

logo = r'''___________                        _________                      __  .__    .__
\__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____
  |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\
  |    |  \___  ||  |_> >  ___/   /        (  <_> )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  >
  |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  /
          \/     |__|        \/          \/             \/     \/          \/        \//_____/   '''

difficulty = 0

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

if choice.lower() == "easy":
    difficulty = 10
elif choice.lower() == "hard":
    difficulty = 5
else:
   print("Invalid command. Try again.")
   exit()

def guess_number(guesses):
    number_to_guess = random.randint(1, 100)

    for num in range(guesses):
        guess = int(input("Make a guess: "))
        remaining = guesses - num - 1
        if guess > number_to_guess:
            print("Too high.\nTry again.")
        elif guess < number_to_guess:
            print("Too low.\nTry again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess}")
            return
        if remaining > 0:
            print(f"You have {remaining} attempts remaining to guess the number")
    print(f"\nYou lose. The number was {number_to_guess}")

guess_number(difficulty)





