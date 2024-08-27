from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)

        if drink is not None:
            is_resource_sufficient = coffee_maker.is_resource_sufficient(drink)

            if is_resource_sufficient:

                payment_accepted = money_machine.make_payment(drink.cost)

                if payment_accepted:
                    coffee_maker.make_coffee(drink)
