from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffe_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


def take_input():
    ask = input("What would you like? (espresso/latte/cappuccino): ")
    while ask != "off":
        if ask == "report":
            coffe_maker.report()
            money_machine.report()
        elif ask == "espresso" or ask == "latte" or ask == "cappuccino":
            drink = menu.find_drink(ask)
            can_make = coffe_maker.is_resource_sufficient(drink)
            if can_make:
                is_transaction_successful = money_machine.make_payment(drink.cost)
                if is_transaction_successful:
                    coffe_maker.make_coffee(drink)
        ask = input("What would you like? (espresso/latte/cappuccino): ")
    pass


take_input()
