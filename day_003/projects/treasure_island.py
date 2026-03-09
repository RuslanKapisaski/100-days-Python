#Description
# Your goal today is to build a "Choose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = input("Left or right? \n").lower()
if direction == "right":
    print("Game over.")
elif direction == "left":
    action = input("Swim or wait\n").lower()
    if action == "swim":
        print("Game over.")
    elif action == "wait":
        door = input("Which door? Red, Blue or Yellow? \n")
        if door == "blue" or door == "red":
            print("Game over.")
        elif door == "yellow":
            print("You win!")
        else:
            print("Invalid door.")
    else:
        print("Invalid action.")
else:
    print("Invalid direction.")