resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def take_input():
    ask = input("What would you like? (espresso/latte/cappuccino): ")
    while ask != "off":
        if ask == "report":
            print_report(resource)
        elif ask == "espresso" or ask == "latte" or ask == "cappuccino":
            check_resource(ask, resource)
        else:
            print("Invalid Keyword!")
        ask = input("What would you like? (espresso/latte/cappuccino): ")
    turn_off()




"""
espresso -> 50ml water, 18g coffee
latte -> 200ml water, 24g coffee, 150ml milk
cappuccino -> 250ml water, 24g coffee, 100ml milk

"""


def check_resource(ask, current_resource):
    message = ""
    resource_available = True
    if ask.lower() == "espresso":
        if current_resource["water"] < 50:
            message = "There is not enough water"
            resource_available = False
        elif current_resource["coffee"] < 18:
            message = "There is not enough coffee"
            resource_available = False
    elif ask.lower() == "latte":
        if current_resource["water"] < 200:
            resource_available = False
            message = "There is not enough water"
        elif current_resource["coffee"] < 24:
            message = "There is not enough coffee"
            resource_available = False
        elif current_resource["milk"] < 150:
            message = "There is not enough milk"
            resource_available = False
    elif ask.lower() == "cappuccino":
        if current_resource["water"] < 250:
            resource_available = False
            message = "There is not enough water"
        elif current_resource["coffee"] < 24:
            message = "There is not enough coffee"
            resource_available = False
        elif current_resource["milk"] < 100:
            message = "There is not enough milk"
            resource_available = False
    else:
        pass

    if resource_available:
        check_transaction(ask, current_resource)
    else:
        print(message)


def turn_off():
    return


def print_report(current_resource):
    water = current_resource["water"]
    milk = current_resource["milk"]
    coffee = current_resource["coffee"]
    money = round(current_resource["money"],2)
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: {money}$")
    pass


def check_transaction(ask, current_resource):
    print("please insert coins")
    quarters = input("How many quarters: ")  # 0.25
    dimes = input("how many dimes: ")  # 0.10
    nickles = input("how many nickles: ")  # 0.05
    pennies = input("how many pennies: ")  # 0.01
    total_provided_money = round(
        (0.25 * float(quarters)) + (0.10 * float(dimes)) + (0.05 * float(nickles)) + (0.01 * float(pennies)), 2)
    current_resource["money"] += total_provided_money
    if ask.lower() == "espresso":
        if current_resource["money"] >= 1.50:
            available_money = current_resource["money"]
            change = round(available_money - 1.50, 2)
            print(f"Here is {change}$ in change")
            make_coffee_update_resource(ask, current_resource)
        else:
            transaction_message = "Sorry that's not enough money. Money refunded."
            print(transaction_message)
    elif ask.lower() == "latte":
        if current_resource["money"] >= 2.50:
            available_money = current_resource["money"]
            change = round(available_money - 2.50, 2)
            print(f"Here is {change}$ in change")
            make_coffee_update_resource(ask, current_resource)
        else:
            transaction_message = "Sorry that's not enough money. Money refunded."
            print(transaction_message)
    elif ask.lower() == "cappuccino":
        if current_resource["money"] >= 3.50:
            available_money = current_resource["money"]
            change = round(available_money - 3.50, 2)
            print(f"Here is {change}$ in change")
            make_coffee_update_resource(ask, current_resource)
        else:
            transaction_message = "Sorry that's not enough money. Money refunded."
            print(transaction_message)
    else:
        pass


"""
espresso -> 50ml water, 18g coffee
latte -> 200ml water, 24g coffee, 150ml milk
cappuccino -> 250ml water, 24g coffee, 100ml milk

"""


def make_coffee_update_resource(ask, current_resource):
    if ask.lower() == "espresso":
        current_resource["water"] -= 50
        current_resource["coffee"] -= 18
        current_resource["money"] -= 1.50
        print("Here is your espresso")
    elif ask.lower() == "latte":
        current_resource["water"] -= 200
        current_resource["coffee"] -= 24
        current_resource["milk"] -= 150
        current_resource["money"] -= 2.50
        print("Here is your latte")
    elif ask.lower() == "cappuccino":
        current_resource["water"] -= 250
        current_resource["coffee"] -= 24
        current_resource["milk"] -= 100
        current_resource["money"] -= 3.00
        print("Here is your cappuccino")
    else:
        pass


take_input()