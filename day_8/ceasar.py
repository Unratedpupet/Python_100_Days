from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


print(logo)

# Combine the encrypt() and decrypt() functions into a single function called caesar().
def ceasar(text, shift, direction):
    translated_message = ""

    # Normalize the shift to ensure it wraps around the alphabet
    shift = shift % 26

    if direction == "decode":
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_base = ord("a") if char.islower() else ord("A")
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            translated_message += new_char
        else:
            translated_message += char

    print(f"The {direction}d text is: {translated_message}")


cipher_run = True
while cipher_run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(text, shift, direction)

    question = input("Do you want to continue? (y/n). ").lower()
    if question == "y":
        continue
    else:
        break
