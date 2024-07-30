alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
  
    encrypted_list = []
    encrypted_message = ""
    # Changes the string to a list for indexing
    for char in text:
        encrypted_list.append(char)
    
    # Shift the letter by the shift amount, and add it to a new string.
    for char in encrypted_list:
        new_char_index = alphabet.index(char) + shift
        encrypted_message += alphabet[new_char_index]
    
    print(f"The encoded text is {encrypted_message}")



#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    encrypted_list = []
    decrypted_message = ""

    for char in text:
        encrypted_list.append(char)

    for char in encrypted_list:
        new_char_index = alphabet.index(char) + 26 - shift
        decrypted_message += alphabet[new_char_index]

    print(f"The decoded text is {decrypted_message}.")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print("Please choose 'encode' or 'decode'.")
