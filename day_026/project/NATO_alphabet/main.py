import pandas

nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_nato_aplabet():
    user_input = input("Enter a word: ").upper()
    try:
        result = [nato_dict[letter] for letter in user_input]
    except KeyError as err:
        print(f"Sorry, only letters of alphabet, please. {err} not valid input!")
        generate_nato_aplabet()
    else:
        print(result)

generate_nato_aplabet()