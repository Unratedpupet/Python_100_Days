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
        

hangman_word = chose_word()
hangman_blanks = word_to_blanks(hangman_word)

print(hangman_blanks)


