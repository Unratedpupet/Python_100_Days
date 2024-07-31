from art import logo

bidding = {}


def clear():
    """
    Makeshift clear command to clear screen.
    """
    print("\n" * 50)


def add_bid(name, bid):
    """
    Adds the bid to the bidding dictionary

    Args:
        name (string): The name of the bidder.
        bid (int): The bid amount.
    """
    bidding[name] = bid


def find_winning_bid():
    """
    Iterates through the bidding dictionary to find the highest bid and prints the highest bidder.
    """
    highest_bid = 0
    highest_bid_name = ""
    for name in bidding:
        if bidding[name] > highest_bid:
            highest_bid = bidding[name]
            highest_bid_name = name
    print(f"The winner is {highest_bid_name} with a bid of ${highest_bid}!")


# Main loop variable
is_open = True

print(logo)
print("Welcome to the secret auction program.")
# Main loop
while is_open:

    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))

    add_bid(name, bid)

    # If there are more bidders, clears the screen, and keeps the loop going.
    more_bidders = input("Are there any other bidders? y/n\n")
    if more_bidders == "y":
        clear()
    else:
        is_open = False

find_winning_bid()
