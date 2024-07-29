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
    if letter not in guesses:
        if letter in hangman_word:
            print(f"{letter} is in the word.")
        else:
            print(f"{letter} is no in the word.")
    else:
        print(f"You have already guessed the letter {letter}. Please try again.")
    guesses.add(letter)



game_state = True
hangman_word = chose_word()
hangman_blanks = word_to_blanks(hangman_word)
guesses = set()

while game_state:
    

    user_guess = input("Please guess a letter: ").lower()
    check_guess(user_guess)


