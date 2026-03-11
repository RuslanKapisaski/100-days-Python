# Password Generator Project

# Description

# Easy Version
# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants
# 4 letters 2 symbols and 3 numbers then the password might look like this: fgdx$*924
# You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well.
# Try to solve this problem first.

# Hard Version
# When you've completed the easy version, you're ready to tackle the hard version.
# In the advanced version of this project the final password does not follow a pattern. So the example above might look like this: x$d24g*k9
# And every time you generate a password, the positions of the symbols, numbers, and letters are different.

import random

letters = [
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+','-','_','=','?','@']

# Easy Version - 4 letters 2 symbols and 3 numbers then the password might look like this: fgdx$*924
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_length = nr_letters + nr_symbols + nr_numbers
my_easy_pass = " "

if nr_letters < 1:
    print("Invalid number of letters")
else:
    for letter in range(1, nr_letters + 1):
        my_easy_pass += random.choice(letters)
    for symbol in range(1, nr_symbols + 1):
        my_easy_pass += random.choice(symbols)
    for number in range(1, nr_numbers + 1):
        my_easy_pass += random.choice(numbers)

print(f"Easy version: {my_easy_pass}")


# Hard version
print("\nWelcome to the PyPassword Generator Advanced!")
nr_letters = int(input("How many letters would you like in your advanced password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

my_hard_pass = " "
pass_container = []
if nr_letters < 1:
    print("Invalid number of letters")
else:
    for letter in range(1, nr_letters + 1):
        pass_container += random.choice(letters)
    for symbol in range(1, nr_symbols + 1):
        pass_container += random.choice(symbols)
    for number in range(1, nr_numbers + 1):
        pass_container += random.choice(numbers)

random.shuffle(pass_container)
my_hard_pass = "".join(pass_container)
print(f"Hard version: {my_hard_pass}")