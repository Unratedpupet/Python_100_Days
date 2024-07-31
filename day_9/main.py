from art import logo

bidding = {}

def clear():  # Prints 50 blank lines
    print("\n" * 50)

def add_bid(name, bid):
    bidding[name] = bid

def find_winning_bid():
    highest_bid = 0
    highest_bid_name = ""
    for name in bidding:
        if bidding[name] > highest_bid:
            highest_bid = bidding[name]
            highest_bid_name = name
    print(f"The winner is {highest_bid_name} with a bid of ${highest_bid}!")

is_open = True

while is_open:


    print("Welcome to the secret auction program.")
    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))

    add_bid(name, bid)

    more_bidders = input("Are there any other bidders? y/n\n")
    if more_bidders == 'y':
        clear()
    else:
        is_open = False

find_winning_bid()
