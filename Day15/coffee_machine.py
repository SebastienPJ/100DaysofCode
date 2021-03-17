from data import MENU, resources


def report(money_in_coffers):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money_in_coffers}")


def check_resources(coffee_choice):

    water_needed = MENU[coffee_choice]["ingredients"]["water"]
    coffee_needed = MENU[coffee_choice]["ingredients"]["coffee"]
    water_in_machine = resources["water"]
    milk_in_machine = resources["milk"]
    coffee_in_machine = resources["coffee"]

    if "milk" in MENU[coffee_choice]["ingredients"]:
        milk_needed = MENU[coffee_choice]["ingredients"]["milk"]
        if milk_needed > milk_in_machine:
            print("Sorry there is not enough milk.")
            return False

    if water_needed > water_in_machine:
        print("Sorry there is not enough water.")
        return False

    elif coffee_needed > coffee_in_machine:
        print("Sorry there is not enough coffee.")
        return False

    else:
        return True


def process_coin():
    """Calculates money inserted into machine returns total money inserted"""
    print("Please insert coins.")
    total_quarters = int(input("how many quarters: ")) * 0.25
    total_dimes = int(input("how many dimes: ")) * 0.1
    total_nickels = int(input("how many nickles: ")) * 0.05
    total_pennies = int(input("how many pennies: ")) * 0.01
    return total_quarters + total_dimes + total_nickels + total_pennies


def successful_transaction(user_money, coffee_chosen):
    """Evaluates whether money inserted equals the cost of coffee chosen. Returns True if money is enough to
    buy the coffee."""
    cost_coffee_chosen = MENU[coffee_chosen]["cost"]
    if user_money >= cost_coffee_chosen:
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded.")


def make_coffee(coffee_chosen, money_in):
    """Makes desired coffee, deducts resources used from resources, gives change back to user,
    returns money to be added to machine coffers"""
    resources["water"] -= MENU[coffee_chosen]["ingredients"]["water"]
    if "milk" in MENU[coffee_chosen]["ingredients"]:
        resources["milk"] -= MENU[coffee_chosen]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_chosen]["ingredients"]["coffee"]
    change_to_give = round(money_in - MENU[coffee_chosen]["cost"], 2)
    print(f"Here is ${change_to_give} in change.")
    print(f"Here is your {coffee_chosen} ☕ Enjoy!")
    return MENU[coffee_chosen]["cost"]


def coffee_machine():
    coffers = 0
    machine_on = True
    while machine_on:
        user_choice = input("   What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "report":
            report(coffers)
        elif user_choice == "off":
            machine_on = False
        elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
            if check_resources(user_choice):
                money_inserted = process_coin()
                if successful_transaction(money_inserted, user_choice):
                    coffers += make_coffee(user_choice, money_inserted)


coffee_machine()



