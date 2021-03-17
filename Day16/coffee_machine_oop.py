from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
drink = Menu()
processor = CoffeeMaker()
payment = MoneyMachine()

while is_on:
    choice = input(f"What would you like? ({drink.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        processor.report()
        payment.report()
    else:
        chosen_drink = drink.find_drink(choice)
        if processor.is_resource_sufficient(chosen_drink):
            if payment.make_payment(chosen_drink.cost):
                processor.make_coffee(chosen_drink)


# a = Menu()
#
# b = a.find_drink("latte")
#
# print(b.cost)
#
# c = CoffeeMaker()
# d = CoffeeMaker()
# print(c.report())
# if c.is_resource_sufficient(b):
#     c.make_coffee(b)
#     print(c.report())
#
# e = MoneyMachine()
# print(e.report())
# e.make_payment(b.cost)
