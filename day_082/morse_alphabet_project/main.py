from logo import Logo
from alphabet import morse_alphabet

print(Logo)

def splitWords(userInput):
    return userInput.split(' ')

def encrypt(userInput):
    words = userInput.split(' ')
    encrypted_words = []
    for word in words:
        encrypted_chars = []
        for char in word:
            if char in morse_alphabet:
                encrypted_chars.append(morse_alphabet[char])
            else:
                encrypted_chars.append('?')
        encrypted_words.append(' '.join(encrypted_chars))
    return ' / '.join(encrypted_words)

def decrypt(encInput):
    reverse_alphabet = {value: key for key, value in morse_alphabet.items()}

    words = encInput.split(' / ')
    decrypted_words = []
    for word in words:
        chars = word.split(' ')
        decrypted_chars = []
        for code in chars:
            if code in reverse_alphabet:
                decrypted_chars.append(reverse_alphabet[code])
            else:
                decrypted_chars.append('?')
        decrypted_words.append(''.join(decrypted_chars))
    return ' '.join(decrypted_words).lower()

def run(command):
    if command == 'e':
        userInput = input("Enter a message: ")
        try:
            result = encrypt(userInput.upper())
            print(f"Encrypted message: {result}")
        except KeyError as e:
            print(f"Unknown character: {e}")

    elif command == 'd':
        userInput = input("Enter a message: ")
        try:
            result = decrypt(userInput)
            print(f"Decrypted message: {result}")
        except Exception as e:
            print(f"Decryption failed: {e}")

while True:
    command = input('Select operation: "e" encrypt / "d" decrypt / "exit" quit: ').strip().lower()

    if command == 'exit':
        print("Closing the program..")
        break
    elif command in ('e', 'd'):
        run(command)
    else:
        print('Invalid command. Use "e", "d", or "exit".')
