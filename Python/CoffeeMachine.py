MENU = {
    "espresso": {
        "ingridents": {
            "water": 50,
            "coffee": 18,
        },
    "cost": 2,
    },
    "latte": {
        "ingridents": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappauccino": {
        "ingridents": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 1000,
    "milk": 700,
    "coffee": 800,
}

def is_resource_sufficient(order_ingriedents):
    """ Returns True when order can be made , False when ingridients are insufficient"""
    for item in order_ingriedents:
        if order_ingriedents[item] >= resources[item]:
            print(f"Sorry there is not enought {item}")
            return False
    return True


def process_coins():
    """ Returns the toal calculated from coins inerted """
    print("Please Enter Coins" )
    total = int(input("How many quarters ?:  ")) * 0.25
    total += int(input("How many dimes ?:  ")) * 0.1
    total += int(input("How many nickes ?:  ")) * 0.05
    total += int(input("How many pennies ?:  ")) * 0.01
    return total


def is_transaction_succesful(money_received, drink_cost):
    """ Return True when the paymetn is accepted , or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the change: {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry thats 's not enough money . Money refuned")
        return False


def make_coffe (drink_name, order_indridents):
    for item in order_indridents:
        resources[item] -= order_indridents[item]
    print(f"Here is your {drink_name} ")




profit = 0
is_on = True


while is_on:
    choice = input("what would you like ? (espresso/latte/cappauccino): ")
    if choice == "off":
        is_on = False 
    elif choice == "report":
        print(f"water: {resources['water']}ml" )
        print(f"milk: {resources['milk']}ml" )
        print(f"coffee: {resources['coffee']}g" )
        print(f"Money: {profit}" )
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingridents"]):
            payment = process_coins()
            is_transaction_succesful(payment, drink["cost"])
            make_coffe(choice, drink["ingridents"])

        









   