logo = r'''                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ '''
import random

words = [
    "apple",
    "banana",
    "orange",
    "grape",
    "pineapple",
    "strawberry",
    "watermelon",
    "computer",
    "keyboard",
    "monitor",
    "python",
    "programming",
    "developer",
    "algorithm",
    "function",
    "variable",
    "internet",
    "network",
    "database",
    "software",
    "mountain",
    "river",
    "forest",
    "desert",
    "island",
    "ocean",
    "castle",
    "dragon",
    "knight",
    "treasure"
]

stages = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]

random_word = random.choice(words)
is_word_guessed = False
lives = 6

def draw_hang_man(lives):
    draw = stages[6 - lives]
    return draw

def encrypt_word(word):
    return ["_"] * len(word)

def check_letters(character, random_word, encrypted, lives):
    is_correct = False

    for i in range(len(random_word)):
        if random_word[i] == character:
            encrypted[i] = character
            is_correct = True

    is_word_guessed = "_" not in encrypted

    return is_correct, is_word_guessed

encrypted = encrypt_word(random_word)

print(logo)

while lives > 0:
    print("Word to guess: ", " ".join(encrypted))
    guess_letter = input("Guess a letter: ").lower()

    is_correct, is_word_guessed = check_letters(guess_letter, random_word, encrypted, lives)

    if is_correct:
        print(f"You've already guessed {guess_letter}")

    else:
        lives -= 1
        print(f"You guessed {guess_letter}, that's not in word. You lose life.")


    if is_word_guessed:
        print("You won! The word was:", random_word)
        break

    print(" ".join(encrypted))
    print(draw_hang_man(lives))

    print(f"{' '.join(['*']*10)}{lives}/6 LIVES LEFT{' '.join(['*']*10)}")

if lives == 0:
    print(draw_hang_man(lives))
    print("You lost! The word was:", random_word)
