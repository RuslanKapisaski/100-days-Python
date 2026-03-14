from logo import asci_logo
from encrypt import encrypt_message
from decrypt import  decrypt_message

print(asci_logo)

while True:
    command = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

    if command.lower() == "encode":
        message = input("Type your message: ")
        shift_number = int(input("Type shift number: "))
        encrypt_message(message, shift_number)

    elif command.lower() == "decode":
        message = input("Type your message: ")
        shift_number = int(input("Type shift number: "))
        decrypt_message(message, shift_number)

    else:
        print("Invalid command, please try again.")

    again = input("Type 'yes' if you want to go again. Otherwise type 'no': ")

    if again.lower() == "no":
        break