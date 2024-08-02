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

random_pick_a = choice(data)
random_pick_b = choice(data)
pick_a_followers = random_pick_a['follower_count']
pick_b_followers = random_pick_b['follower_count']
higher_follower_count = ''

if pick_a_followers > pick_b_followers:
    higher_follower_count = 'a'
else:
    higher_follower_count = 'b'

print(f"Compare A: {random_pick_a['name']}, a {random_pick_a['description']}, from {random_pick_a['country']}")
print(art.vs)
print(f"Against B: {random_pick_b['name']}, a {random_pick_b['description']}, from {random_pick_b['country']}")
answer = input("Who has more followers? Type 'a' or 'b': ")

if answer == higher_follower_count:
    print("You win")
else:
    print("You lose")

