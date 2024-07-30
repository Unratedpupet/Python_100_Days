alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def ceasar(text, shift, direction):
    encrypted_list = []
    translated_message = ""
    # Changes the string to a list for indexing
    for char in text:
        encrypted_list.append(char)
    
    if direction == 'encode':
        for char in encrypted_list:
            new_char_index = alphabet.index(char) + shift
            translated_message += alphabet[new_char_index]
        print(f"The encoded text is {translated_message}")
    elif direction == 'decode':
        for char in encrypted_list:
            new_char_index = alphabet.index(char) + 26 - shift
            translated_message += alphabet[new_char_index]
        print(f"The decoded text is {translated_message}.")




#Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

ceasar(text, shift, direction)
