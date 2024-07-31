############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Flow
# Do you want to play a game of Blackjack? Type 'y' or 'n':  ||| Not going to ask... you opened it, you play it.
# Prints the logo each time
# Shows your cards, in a list format
# Shows dealer first card
# 'h' for hit, 's' for stand
# hit add a new card to your hand
# -> adds new card to your hand, show dealer hand again, if > 21, game ends and dealer wins else ask for next move
# stand ends your hand and shows dealer
# -> Dealer hits if < 16 else stand
# -> if dealer > 21 player wins elif 21 <= dealer <= player dealer wins elif dealer == player draw else player wins
# Ace can be 1 or 11. if ace in hand and hand > 21, convert ace to 1.
# If player hand 10 + 11, auto win.

from random import choice
from art import logo
print(logo)

def draw_card() -> int:
    """Draws a random card

    Returns:
        int: Randomly selected card from the cards deck
    """
    return choice(cards)

def bust(hand: list[int]) -> bool:
    """Checks to see if the hand is a bust.

    Args:
        hand (list): The hand to be checked.

    Returns:
        bool: True if over 21. False if < 21.
    """
    return sum(hand) > 21

def dealer_play() -> int:
    while sum(dealer_hand) < 16:
        dealer_hand.append(draw_card())

    total = sum(dealer_hand)

    if bust(dealer_hand):
        print(f"Dealer busts with {total}. You win!")
        return total
    else:
        return total


def dealer_win():
    print(f"Dealer wins with {sum(dealer_hand)}.")

def blackjack(hand: list) -> bool:
    """Checks to see if blackjack occured

    Args:
        hand (list): The hand to be checked.

    Returns:
        bool: True if 21, False if not.
    """
    return sum(hand) == 21

def player_start():
    player_hand.append(draw_card())
    player_hand.append(draw_card())
    if blackjack(player_hand):
        player_win()

player_hand = []
dealer_hand = []

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_playing = True

dealer_hand.append(draw_card())
player_start()

print(f"Your hand is {player_hand}")
print(f"The dealer's first card is {dealer_hand}")

while is_playing:

    play = input("'h' for hit, 's' for stand")
    if play == "h":
        player_hand.append(draw_card())
        print(f"Your hand is now {player_hand}")
        if blackjack(player_hand):
            is_playing = player_win()
    else:
        dealer_play()


