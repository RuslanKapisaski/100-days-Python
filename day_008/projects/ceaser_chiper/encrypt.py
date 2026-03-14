
def encrypt_message(original_text,shift_amount):
    ascii_value = ""
    encrypted_message = ""
#Shift ASCII code characters
    for char in original_text:
        ascii_value = ord(char)
        shifted = ascii_value + shift_amount
        encrypted_message += chr(shifted)
    output_message = print(f"Here is the encoded result: {encrypted_message}")
    return output_message
