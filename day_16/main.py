from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_machine_on = True

while is_machine_on:
    command = input(f"What would you like? {menu.get_items()}")

    if command == "off":
        break
    elif command == "latte":
        order = menu.find_drink(command)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
    elif command == "espresso":
        order = menu.find_drink(command)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
    elif command == "cappuccino":
        order = menu.find_drink(command)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
    elif command == "report":
        coffee_maker.report()
        money_machine.report()
