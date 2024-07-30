## Making a hangman game

import random

# First challenge is to make a list of random words, make blanks equal to the number of letters in the word, and have user guess.

word_list = ['python', 'javascript', 'hangman', 'development', 'programming', 'algorithm', 'datastructure', 'variable', 'function', 'object']

# Chose the random word

def chose_word():
    return random.choice(word_list)



# Changes the letters into '_' to allow for guesses.
def word_to_blanks(word):
    blanks = ''
    for char in word:
        blanks += '_ '
    return blanks
        
# Checks to see if the letter is in the hangman word.
def check_guess(letter):
    if letter in guesses:
        print(f"You have already guessed the letter {letter}. Please try again.")
    else:
        for char in hangman_word:
            if char == letter:
                print(f"{letter} is correct.")
    # Addes guessed letter to the guessed letters.    
    guesses.add(letter)



game_state = True
hangman_word = chose_word()
hangman_blanks = word_to_blanks(hangman_word)
guesses = set()

while game_state:
    
    print(hangman_word)
    print(hangman_blanks)
    print(f"You have already guessed: {guesses}")
    user_guess = input("Please guess a letter: ").lower()
    check_guess(user_guess)


