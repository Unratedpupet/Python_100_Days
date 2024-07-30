## Making a hangman game

import random
attempts = 6

# First challenge is to make a list of random words, make blanks equal to the number of letters in the word, and have user guess.

word_list = ['python', 'javascript', 'hangman', 'development', 'programming', 'algorithm', 'datastructure', 'variable', 'function', 'object']

# Chose the random word

def chose_word():
    return random.choice(word_list)



# Changes the letters into '_' to allow for guesses.
def word_to_blanks(word):
    blanks = []
    for char in word:
        blanks.append("_")
    return blanks
        
# Checks to see if the letter is in the hangman word.
def check_guess(letter):
    if letter in guesses:
        print(f"You have already guessed the letter {letter}. Please try again.")
    else:
        if letter in hangman_word:
            
            # Initiates an index to go through the list.
            index = 0
            for char in hangman_word:
                # If the letter equals the char in the hangman_word, it changes the blank to it, then increments the index.
                if char == letter:
                    hangman_blanks[index] = letter
                index += 1
        else: 
            attempts -= 1        
                

    # Addes guessed letter to the guessed letters.    
    guesses.add(letter)



game_state = True
hangman_word = chose_word()
hangman_blanks = word_to_blanks(hangman_word)
guesses = set()


while attempts > 0:
    
    print(f"You have {attempts} attempts left.")
    print(hangman_word)
    print(hangman_blanks)
    print(f"You have already guessed: {guesses}")
    user_guess = input("Please guess a letter: ").lower()
    check_guess(user_guess)
    

