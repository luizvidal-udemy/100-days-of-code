from typing import Dict, TypedDict, NotRequired


class Ingredient(TypedDict):
    water: float
    coffee: float
    milk: NotRequired[float]


class Item(TypedDict):
    ingredients: Ingredient
    cost: float


class Resources(TypedDict):
    water: float
    milk: float
    coffee: float
    money: float


def calculate_change(
    price: float,
    quarter: float,
    dimes: float,
    nickels: float,
    pennies: float
):
    total = (quarter * 0.25) + (dimes * 0.10) + \
        (nickels * 0.05) + (pennies * 0.01)

    return round(total - price, 2)


def verify_insufficient_resources(item: Item, resources: Resources):
    ingredients = item["ingredients"]

    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            return ingredient


def show_report(resources: Resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def make_coffee(item: Item, resources: Resources):
    ingredients = item["ingredients"]

    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

    resources["money"] += item["cost"]


MENU: Dict[str, Item] = {
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

resources: Resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# resources: Resources = {
#     "water": 1,
#     "milk": 1,
#     "coffee": 1,
#     "money": 0
# }


action = ""

while action != "off":

    coffe_options = [
        "espresso",
        "latte",
        "cappuccino"
    ]

    action = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    if action == "report":
        show_report(resources)

    elif action == "off":
        print("Thanks for using the Coffee Machine. Goodbye!")

    elif action in coffe_options:
        coffee = MENU[action]

        insufficient_resource = verify_insufficient_resources(
            coffee, resources
        )

        if insufficient_resource is not None:
            print(f"Sorry there is not enough {insufficient_resource}.")

        else:
            print("Please insert coins.")

            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            change = calculate_change(
                coffee["cost"],
                quarters,
                dimes,
                nickles,
                pennies
            )

            if change >= 0:
                print(
                    f"Here is ${change:.2f} in change."
                ) if change > 0 else None

                make_coffee(coffee, resources)

                print("Here's your " + action + " ☕. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")
