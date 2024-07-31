from art import logo

bidding = {}

def clear():  # Prints 50 blank lines
    print("\n" * 50)

def add_bid(name, bid):
    bidding[name] = bid

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

print(bidding)