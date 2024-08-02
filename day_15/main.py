MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

bank = 5.00

def report():
    for key, value in resources.items():
        print(f"{key}: {value}")
    print(f"Cash: {bank}")

def make_espresso():
    print("Made espresso")

def make_latte():
    print("Made latte")

def make_cappuccino():
    print("Made cappuccino")

on = True

while on:
    command = input("What would you like? espresso/latte/cappuccino\n")

    if command == "off":
        on = False
    elif command == "report":
        report()
    elif command == "espresso":
        make_espresso()
    elif command == "latte":
        make_latte()
    elif command == "cap":
        make_cappuccino()
    else:
        print("Please enter a valid command.")
