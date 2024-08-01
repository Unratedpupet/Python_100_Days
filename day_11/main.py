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

def draw_card() -> int:
    """Draws a random card

    Returns:
        int: Randomly selected card from the cards deck
    """
    return choice(cards)

def bust(hand: list[int]) -> bool:
    """Checks to see if the hand is a bust after adjusting for Aces.

    Args:
        hand (list[int]): The hand to be checked.

    Returns:
        bool: True if over 21, False if 21 or under.
    """
    hand = adjust_for_ace(hand)
    return sum(hand) > 21

def dealer_play() -> bool:
    """Simulates the dealer's play and determines if the dealer busts or stands."""
    while sum(dealer_hand) < 16:
        dealer_hand.append(draw_card())
        print(f"Dealer hits to make hand {dealer_hand}")

    dealer_hand = adjust_for_ace(dealer_hand)
    if bust(dealer_hand):
        print(f"Dealer busts with {sum(dealer_hand)}. You win!")
        return True
    else:
        return False

def dealer_win():
    """Just prints out dealer wins."""
    print(f"Dealer wins with {sum(dealer_hand)}.")

def blackjack(hand: list) -> bool:
    """Checks to see if blackjack occurred

    Args:
        hand (list): The hand to be checked.

    Returns:
        bool: True if 21, False if not.
    """
    return sum(hand) == 21

def player_start() -> bool:
    """Creates the player start by drawing two cards and checking for blackjack."""
    player_hand.append(draw_card())
    player_hand.append(draw_card())
    if blackjack(player_hand):
        print(f"Player got blackjack with a hand of {player_hand}!")
        return False
    else:
        return True

def new_game() -> bool:
    """Clears both hands and asks if you want to start a new game.

    Returns:
        bool: The T/F response to starting a new game.
    """
    player_hand.clear()
    dealer_hand.clear()
    result = input("Would you like to keep playing? y/n\n").lower()
    return result == 'y'

def adjust_for_ace(hand: list[int]) -> list[int]:
    """Adjusts the hand for Aces to prevent busting.

    Args:
        hand (list[int]): The hand to be adjusted.

    Returns:
        list[int]: The adjusted hand.
    """
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return hand

player_hand = []
dealer_hand = []

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_playing = True

while is_playing:
    print(logo)
    dealer_hand.append(draw_card())
    if player_start():
        while True:
            print(f"Your hand is {player_hand}")
            print(f"The dealer's first card is {dealer_hand}") 

            play = input("'h' for hit, 's' for stand: ").lower()
            if play == "h":
                player_hand.append(draw_card())
                print(f"Your hand is now {player_hand}")
                if bust(player_hand):
                    print(f"You bust with the {sum(player_hand)}")
                    break
            elif play == "s":
                if dealer_play():
                    break
                player_total = sum(player_hand)
                dealer_total = sum(dealer_hand)
                print(f"Dealer's hand is {dealer_hand} with a total of {dealer_total}")
                print(f"Your hand is {player_hand} with a total of {player_total}")

                if dealer_total > 21 or player_total > dealer_total:
                    print("You win!")
                elif dealer_total == player_total:
                    print("It's a draw.")
                else:
                    dealer_win()
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")
        is_playing = new_game()
    else:
        is_playing = new_game()
