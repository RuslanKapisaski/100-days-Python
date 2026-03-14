def decrypt_message(encrypted_text, shift_amount):
    ascii_value = ""
    decrypted_message = ""
#Shift ASCII code characters
    for char in encrypted_text:
        ascii_value = ord(char)
        shifted = ascii_value - shift_amount
        decrypted_message += chr(shifted)
    output_message = print(f"Here is the decoded result: {decrypted_message}")
    return output_message

    return decrypted_message
