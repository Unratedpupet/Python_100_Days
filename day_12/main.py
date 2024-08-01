#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import choice
from art import logo

def choose_number() -> int:
    return choice(range(0, 101))


def lose_life():
    return lives - 1

EASY_LEVEL = 10 
HARD_LEVEL = 5

lives = 0

print(logo)

secret_number = (choose_number())

print(secret_number)

choose_difficulty = input("Choose a level. Easy 'e' or Hard 'h': ")

if choose_difficulty == 'e':
    lives = EASY_LEVEL
elif choose_difficulty == 'h':
    lives = HARD_LEVEL
else:
    print("Please enter 'e' or 'h'.")



player_guess = 0

while player_guess != secret_number:
    player_guess = int(input("What is your guess: "))

    if player_guess > secret_number:
        print(f"You guessed {player_guess}, that was too high.")
        lose_life()
        print(f"You have {lives} lives left.")
    else:
        print(f"You guessed {player_guess}, that is too low.")
        lose_life()
        print(f"You have {lives} lives left.")