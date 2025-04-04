menu = {
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

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25
}


# TODO:
#   5. Process coins.
#       a. If there are sufficient resources to make the drink selected, then the program should
#          prompt the user to insert coins.
#       b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#       c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#          pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO:
#   6. Check transaction successful?
#       a. Check that the user has inserted enough money to purchase the drink they selected.
#          E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#          program should say “Sorry that's not enough money. Money refunded.”.
#       b. But if the user has inserted enough money, then the cost of the drink gets added to the
#          machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#          Water: 100ml
#          Milk: 50ml
#          Coffee: 76g
#          Money: $2.5
#       c. If the user has inserted too much money, the machine should offer change.
#          E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
#          places.

# TODO:
#   7. Make Coffee.
#       a. If the transaction is successful and there are enough resources to make the drink the
#          user selected, then the ingredients to make the drink should be deducted from the
#          coffee machine resources.
#          E.g. report before purchasing latte:
#          Water: 300ml
#          Milk: 200ml
#          Coffee: 100g
#          Money: $0
#          Report after purchasing latte:
#          Water: 100ml
#          Milk: 50ml
#          Coffee: 76g
#          Money: $2.5
#       b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
#          latte was their choice of drink.


def ingredients_print(coffee):

    ingredients = menu[coffee]["ingredients"].keys()

    print("\t\tIngredients:")
    for ingredient in ingredients:
        print(f"\t\t\t{ingredient.capitalize()}: {menu[coffee]['ingredients'][ingredient]}")


def resources_check(coffee):

    enough = True

    if coffee == "espresso":

        if menu['espresso']['ingredients']['water'] < resources['water']:
            print("\tNot enough water")
            enough = False

        if menu['espresso']['ingredients']['coffee'] < resources['coffee']:
            print("\tNot enough coffee")
            enough = False

    elif coffee == "latte":

        if menu['latte']['ingredients']['water'] < resources['water']:
            print("\tNot enough water")
            enough = False

        if menu['latte']['ingredients']['milk'] < resources['milk']:
            print("\tNot enough milk")
            enough = False

        if menu['latte']['ingredients']['coffee'] < resources['coffee']:
            print("\tNot enough coffee")
            enough = False

    elif coffee == "cappuccino":

        if menu['cappuccino']['ingredients']['water'] < resources['water']:
            print("\tNot enough water")
            enough = False

        if menu['cappuccino']['ingredients']['milk'] < resources['milk']:
            print("\tNot enough milk")
            enough = False

        if menu['cappuccino']['ingredients']['coffee'] < resources['coffee']:
            print("\tNot enough coffee")
            enough = False

    if enough:
        print()

    return enough


while True:

    print("Menu:")
    print(f"\t1. Espresso          ${menu['espresso']['cost']}")
    print(f"\t2. Latte             ${menu['latte']['cost']}")
    print(f"\t3. Cappuccino        ${menu['cappuccino']['cost']} ")
    print("\t4. Options")
    print()

    pick = input("Your pick: ")
    print()

    if pick.lower() == "espresso" or pick == '1':
        coffee = "espresso"

        print("\tEspresso")
        print(f"\t\tCost: ${menu['espresso']['cost']}")
        print()

        enough = resources_check(coffee)

        print("Please insert coins")

    elif pick.lower() == "latte" or pick == '2':
        coffee = "latte"

        print("\tLatte")
        print(f"\t\tCost: ${menu['latte']['cost']}")
        print()

        enough = resources_check(coffee)

        print("Please insert coins")

    elif pick.lower() == "cappuccino" or pick == '3':
        coffee = "cappuccino"

        print("\tCappuccino")
        print(f"\t\tCost: ${menu['cappuccino']['cost']}")
        print()

        enough = resources_check(coffee)

        print("Please insert coins")

    elif pick.lower() == "options" or pick == '4':
        print("\tOptions:")
        print("\t\t1. Menu")
        print("\t\t2. Resources")
        print("\t\t3. Espresso ingredients")
        print("\t\t4. Latte ingredients")
        print("\t\t5. Cappuccino ingredients")
        print("\t\t6. Off")
        print()

        choice = input("Your pick: ")
        print()

        if choice.lower() == "menu" or choice == '1':
            continue

        elif choice.lower() == "resources" or choice == '2':
            print("\tResources:")
            print(f"\t\tWater: {resources['water']}")
            print(f"\t\tMilk: {resources['milk']}")
            print(f"\t\tCoffee: {resources['coffee']}")

        elif choice.lower() == "espresso" or choice == '3':
            print("\tEspresso")
            ingredients_print("espresso")

        elif choice.lower() == "latte" or choice == '4':
            print("\tLatte")
            ingredients_print("latte")

        elif choice.lower() == "cappuccino" or choice == '5':
            print("\tCappuccino")
            ingredients_print("cappuccino")

        elif choice.lower() == "off" or choice == '6':
            break

    else:
        print("\tYour pick is not one of the options")
    print()
