import random
from logo import logo_temp
from words import word_list
from stages import hangman_stages

def draw_hang_man(lives):
    draw = hangman_stages[6 - lives]
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

random_word = random.choice(word_list)
is_word_guessed = False
lives = 6

encrypted = encrypt_word(random_word)

stars_temp = ' '.join(['*'] * 10)

print(logo_temp)

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
        print(f"\n{stars_temp} - You won! The word was {random_word} - {stars_temp}")

        break

    print(" ".join(encrypted))
    print(draw_hang_man(lives))
    print(f"{stars_temp}{lives}/6 LIVES LEFT{stars_temp}")

if lives == 0:
    print(f"\n{stars_temp} - You lost! The word was {random_word} - {stars_temp}")

