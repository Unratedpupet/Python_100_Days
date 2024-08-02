import art
from game_data import data
from random import choice

"""

Higher vs Lower game.

First print out the logo
print out the first item from game_data
print the vs art
print the second item from game_data

ask the use who has more followers

game_data items are a list of dictionaries with the following keys:
    name
    follower_count
    description
    country

keep score of how many gotten right.
Game ends first time player is wrong
    display message and final score.


"""

print(art.logo)

random_pick_1 = choice(data)
random_pick_2 = choice(data)

print(f"{random_pick_1['name']}, a {random_pick_1['description']}, from {random_pick_1['country']}")

