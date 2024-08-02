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
    },
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


def check_resources(drink: str) -> bool:
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(
                f"Not enough {ingredient} to make {drink}. Please notify the coffee admin."
            )
            return False
    print(f"Able to make {drink}.")
    return True


def make_drink(drink: str):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount


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
            make_drink(command)
        elif command == "latte":
            check_resources(command)
            make_drink(command)
        elif command == "cappuccino":
            check_resources(command)
            make_drink(command)
        else:
            print("Please enter a valid command.")


operations()
