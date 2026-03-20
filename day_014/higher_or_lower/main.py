from random import sample
from art import header,vs_art
from data import famous_people

def generate_famous_people(people):
    return sample(famous_people,k = people)

famous_person1,famous_person2 = generate_famous_people(2)

print(header)
play_game = True
score = 0

while play_game:
    famous_person3 = generate_famous_people(1)[0]

    print(famous_person3["name"])
    print(f"Compare A: {famous_person1['name']}, {famous_person1['description']}")
    print(vs_art)
    print(f"Compare B: {famous_person2['name']}, {famous_person2['description']}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choice not in ['a','b']:
        print("Invalid option")
        play_game = False
    elif choice == "a":
        if famous_person1['followers'] > famous_person2['followers']:
            score += 1
            famous_person2 = famous_person3
        else:
            play_game = False
    elif choice == "b":
        if famous_person2["followers"] > famous_person1["followers"]:
            score += 1
            famous_person1 = famous_person2
            famous_person2 = famous_person3
        else:
            play_game = False

print(f"\nSorry, that's wrong. Final score: {score}")