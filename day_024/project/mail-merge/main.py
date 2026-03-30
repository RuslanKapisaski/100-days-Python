with open('../mail-merge/Input/Names/invited_names.txt') as invited_names:
    names = invited_names.readlines()

    for name in names:
        name = name.strip()

        with open('../mail-merge/Input/Letters/starting_letter.txt',mode='r') as starting_letter:
            letter = starting_letter.read()
            new_letter = letter.replace("name", f"{name}")

            with open(f'../mail-merge/Output/ReadyToSend/letter_for_{name}.txt',mode='w') as write_fiile:
                write_fiile.write(new_letter)
