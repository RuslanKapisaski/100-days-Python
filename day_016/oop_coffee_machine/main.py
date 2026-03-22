from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while (choice := input("What would you like? (espresso/latte/cappuccino/): ")).lower() != "off":
    if choice == "report":
       coffe_maker.report()
    elif choice in ["espresso", "latte", "cappuccino"]:
        ordered_drink = menu.find_drink(choice)
        is_resource_sufficient = CoffeeMaker.is_resource_sufficient(self=CoffeeMaker(), drink=ordered_drink)
        if coffe_maker.is_resource_sufficient(ordered_drink):
            if money_machine.make_payment(ordered_drink.cost):
                coffe_maker.make_coffee(ordered_drink)
    elif choice not in ["espresso", "latte", "cappuccino","off"]:
            print("Sorry, that's not a valid choice.")







