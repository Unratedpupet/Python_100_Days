## Making a hangman game

import random
import hangman_art
import hangman_words

# First challenge is to make a list of random words, make blanks equal to the number of letters in the word, and have user guess.

word_list = hangman_words.word_list
stage = hangman_art.stages
logo = hangman_art.logo

# Chose the random word


def chose_word():
    return random.choice(word_list)


# Changes the letters into '_' to allow for guesses.
def word_to_blanks(word):
    return ["_"] * len(word)


# Checks to see if the letter is in the hangman word.
def check_guess(letter):
    global attempts
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
            print(f"{letter} was not in the word.")
            attempts -= 1

    # Addes guessed letter to the guessed letters.
    guesses.add(letter)


def check_win():
    global game_state
    if attempts < 1:
        print(f"You lose. The correct answer was {hangman_word}.")
        print(stage[0])
        game_state = False

    if "_" not in hangman_blanks:
        print(f"You win! The correct answer was {hangman_word}")
        game_state = False


def stages():
    global attempts
    match attempts:
        case 6:
            print(stage[6])
        case 5:
            print(stage[5])
        case 4:
            print(stage[4])
        case 3:
            print(stage[3])
        case 2:
            print(stage[2])
        case 1:
            print(stage[1])
        case 0:
            print(stage[0])


game_state = True
hangman_word = chose_word()
hangman_blanks = word_to_blanks(hangman_word)
guesses = set()
attempts = 6


while game_state:

    print(logo)
    stages()
    print(f"You have {attempts} attempts left.")
    print(" ".join(hangman_blanks))
    print(f"You have already guessed: {', '.join(guesses)}")
    user_guess = input("Please guess a letter: ").lower()
    check_guess(user_guess)
    check_win()
