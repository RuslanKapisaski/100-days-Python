#Love Calculator
# This is a difficult challenge! 💪
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number and print it out. e.g. name1 = "Angela Yu" name2 = "Jack Bauer"
#
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5

# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3

# Love Score = 53

# Example Input
# calculate_love_score("Kanye West", "Kim Kardashian")
# Example Output
# 42

def calculate_love_score(name1, name2):
    love_word = "love"
    true_word = "true"
    love_points = 0
    true_points = 0
    combined_names = name1 + name2

    for char in combined_names:
        if char in love_word:
            love_points += 1
        if char in true_word:
            true_points += 1

    message = int(str(true_points) + str(love_points))
    return print(message)


calculate_love_score("Kanye West", "Kim Kardashian")