LOGO = """
   _____ _______       _____  _____  _    _  _____ _  __ _____ 
  / ____|__   __|/\   |  __ \|  __ \| |  | |/ ____| |/ // ____|
 | (___    | |  /  \  | |__) | |  | | |  | | |    | ' /| (___  
  \___ \   | | / /\ \ |  _  /| |  | | |  | | |    |  <  \___ \ 
  ____) |  | |/ ____ \| | \ \| |__| | |__| | |____| . \ ____) |
 |_____/   |_/_/    \_\_|  \_\_____/ \____/ \_____|_|\_\_____/ 
                                                               
                                                               
"""

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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# print the menu coffees -- cost $
print(LOGO)
print("MANU :---")
print(f"espresso :- cost :${MENU["espresso"]["cost"]}")
print(f"latte :- cost :${MENU["latte"]["cost"]}")
print(f"cappuccino :- cost :${MENU["cappuccino"]["cost"]}\n")
print("NOTE : quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01")


def is_resources_sufficient(order_ingredients):
    """# make a function for resource checking"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


def report():
    """make a function for report"""
    for key, value in resources.items():
        print(f"{key} : {value}")
    print(f"Money = ${profit}")


def process_coins():
    print("please insert Coins.....")
    quarters = float(input("How many Quarters")) * 0.25
    dimes = float(input("How many Dimes")) * 0.10
    nickles = float(input("How many Nickles")) * 0.05
    pennies = float(input("How many Pennies")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def make_coffee(drink_name, order_ingredients):
    """deduct the resources from the order ingredients """
    for item in order_ingredients:
        resources[item] -= order_ingredients
    print(f"Here is your {drink_name} ☕ . Enjoy!")


machine_on = True
while machine_on:
    """make A while loop and when the user types off the machine stops"""
    user_prompt = input("what would you like? (espresso/ latte/ cappuccino) ").lower().strip()
    if user_prompt == "off":
        machine_on = False
    elif user_prompt == "report":
        report()
    else:
        drink = MENU[user_prompt]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_prompt, drink["ingredients"])



    # elif user_prompt == "espresso":
    #     espresso()
### or report , the promt should access different functions by diffrent keywords


# i ll have to make different functions for each beverage and a function for report
### check the resources are sufficient when then user orders the drink





#make a function for coint processer def coint_processer()  Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

#Check transaction

#Make Coffee

