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

# def check_espresso():
#     if check_resources("espresso"):
#         print("Made espresso")
#     else:
#         print("Could not make espresso, need more of an item.")

# def check_latte():
#     if check_resources("latte"):
#         print("Made latte")
#     else:
#         print("Could not make latte, need more of an item.")

# def check_espresso():
#     if check_resources("cappuccino"):
#         print("Made cappuccino")
#     else:
#         print("Could not make cappuccino, need more of an item.")

def check_resources(drink: str) -> bool:
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            return False
    print(f"Able to make {drink}.")
    return True




def operations():
    on = True

    while on:
        command = input("What would you like? espresso/latte/cappuccino\n")

        if command == "off":
            on = False
        elif command == "report":
            report()
        elif command == "espresso":
            check_resources(command)
        elif command == "latte":
            check_resources(command)
        elif command == "cappuccino":
            check_resources(command)
        else:
            print("Please enter a valid command.")

operations()