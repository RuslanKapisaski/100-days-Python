import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_choices = [rock,paper,scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if user_input not in range(len(game_choices)):
    print("Invalid choice. Try again from 0 to 2...")
else:
    user_choice = game_choices[user_input]
    pc_choice = random.choice(game_choices)
    print(user_choice)
    print("Computer chose:")
    print(pc_choice)
    if user_choice == pc_choice:
        print("Draw")
    elif user_choice == rock and  pc_choice == paper or user_choice == paper and  pc_choice == scissors or  user_choice == scissors and  pc_choice == rock:
        print("You lose")
    else:
        print("You win")


