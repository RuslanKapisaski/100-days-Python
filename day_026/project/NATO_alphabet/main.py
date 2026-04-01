import pandas

nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()

result = [nato_dict[letter] for letter in user_input if letter.isalpha()]

print(result)
