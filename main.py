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

money = 0.0


# Print report
def print_report():
    for key in resources:
        if key == "coffee":
            print(f"{key} : {resources[key]}g")
        else:
            print(f"{key} : {resources[key]}ml")
    print(f"Money : ${money}")


# Check resources sufficient
def check_resource(drink):
    req_ingredients = MENU[drink]["ingredients"]

    for key in req_ingredients:
        if resources[key] < req_ingredients[key]:
            print(f"Sorry there is not enough {key}.")
            return False

    return True


# Process Coins
def process_coins(drink ):
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickles + pennies
    if total < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return
    global money
    money += MENU[drink]["cost"]

    return total - MENU[drink]["cost"]


def brew(drink):
    ingredients = MENU[drink]["ingredients"]
    for key in ingredients:
        resources[key] -= ingredients[key]
    print(f"Here is your {drink} ☕️. Enjoy!")


def start():
    on = True
    while on:
        drink = input(" What would you like? (espresso/latte/cappuccino): ")
        if drink == "off":
            on = False
        elif drink == "report":
            print_report()
        else:
            if check_resource(drink):
                change = process_coins(drink)
                if change != None:
                    brew(drink)
                    if change > 0:
                        print(f"Here is your change ${round(change, 2)}")



start()