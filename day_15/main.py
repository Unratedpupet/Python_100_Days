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


def charge(drink: str):
    payment_quarters = int(input("Please insert quarters: "))
    payment_dimes = int(input("Please insert dimes: "))
    payment_nickels = int(input("Please insert nickels: "))
    payment_pennies = int(input("Please insert pennies: "))

    total = 0

    total += 0.25 * payment_quarters
    total += 0.10 * payment_dimes
    total += 0.05 * payment_nickels
    total += 0.01 * payment_pennies
    
    change = total - MENU[drink]["cost"]

    if total == MENU[drink]["cost"]:
        print("Exact change, thank you!")
    elif total > MENU[drink]["cost"]:
        print(f"Thank you for your payment of {total:.2f}, your change is : ${change:.2f}.")
    else:
        print(f"Not enough money. A {drink} costs ${MENU[drink]['cost']:.2f}")


def operations():
    on = True

    while on:
        command = input("What would you like? espresso/latte/cappuccino\n")

        if command == "off":
            on = False
        elif command == "report":
            report()
        elif command == "espresso":
            if check_resources(command):
                print(f"Your espresso costs: ${MENU['espresso']['cost']:.2f}")
                charge(command)
                make_drink(command)
        elif command == "latte":
            if check_resources(command):
                print(f"Your espresso costs: ${MENU['latte']['cost']:.2f}")
                charge(command)
                make_drink(command)
        elif command == "cappuccino":
            if check_resources(command):
                print(f"Your espresso costs: ${MENU['cappuccino']['cost']:.2f}")
                charge(command)
                make_drink(command)
        else:
            print("Please enter a valid command.")


operations()
