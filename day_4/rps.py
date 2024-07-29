import random
# Random choice between 1 and 3
comp_choice = random.randint(1,3)

# 1 = rock
# 2 = paper
# 3 = scissor

player_choice = int(input("Welcome to rock, paper, scissors. Please pick 1 for rock, 2 for paper, 3 for scissors: \n"))


def int_to_rps(value):
    if value == 1:
        return "rock"
    elif value == 2:
        return "paper"
    elif value == 3:
        return "scissors"
    else:
        return "Invalid option"

def print_choices():
    print(f"You chose {int_to_rps(player_choice)}.")
    print(f"Computer chose {int_to_rps(comp_choice)}.")

if comp_choice == player_choice:
    print_choices()
    print("It's a draw!")
elif comp_choice == 1 and player_choice == 2:
    print_choices()
    print("You win!")
elif comp_choice == 1 and player_choice == 3:
    print_choices()
    print("Computer wins.")
elif comp_choice == 2 and player_choice == 1:
    print_choices()
    print("Computer wins.")
elif comp_choice == 2 and player_choice == 3:
    print_choices()
    print("You win!")
elif comp_choice == 3 and player_choice == 1:
    print_choices()
    print("You win!")
elif comp_choice == 3 and player_choice == 2:
    print_choices()
    print("Computer wins")
else:
    print("Something went wrong determining a winner.")