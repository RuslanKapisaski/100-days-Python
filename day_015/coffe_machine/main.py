from data import MENU, resources

def check_unit(data):
    if data == "milk":
        return "ml"
    if data == "water":
        return "ml"
    if data == "coffe":
        return "g"
    if data == "money":
        return "$"

def print_report():
     for key in resources:
        unit = check_unit(key)

        if key != "money":
            message = f"{key}: {resources[key]}{unit}"
            print(message)
        else:
            message = f"{key}: {unit}{resources[key]}"
            print(message)

def is_resource_sufficient(data):
    is_sufficient = True
    insufficient_product = ''
    product_ingredients = data["ingredients"]

    for key in product_ingredients:
        if resources[key] < product_ingredients[key]:
            insufficient = key
            is_sufficient = False
            return is_sufficient, insufficient
    return is_sufficient, insufficient_product

def process_coins():
    quarters = int(input("How many quarters?")) #0.25
    dimes = int(input("How many dimes?")) #.10
    nickles = int(input("How many nickles?")) #0.05
    pennies = int(input("How many pennies?"))#0.01
    total = (quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01)

    return total

def prepare_product(item, fee):
    ingredients = item["ingredients"]
    price = item["cost"]

    for key in ingredients:
        resources[key] -= ingredients[key]

    resources["money"] += price
    change = fee - price

    if change > 0:
        print(f"Here is your change: {round(change,2)}.")

while (command := input("What would you like? (espresso/latte/cappuccino): ").lower()) != "off":
    product = ''
    if command=="report":
        print_report()

    if command=="espresso":
        product_name = "espresso"
        product = MENU[product_name]
        is_sufficient, insufficient_product = is_resource_sufficient(product)
        if not is_sufficient:
            print(f"Sorry there is not enough {insufficient_product}.")
        else:
            fee = process_coins()
            if fee < product["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                prepare_product(product, fee)
                print(f"Here is your {product_name}. Enjoy!")

    if command == "latte":
        product_name = "latte"
        product = MENU[product_name]
        is_sufficient, insufficient_product = is_resource_sufficient(product)
        if not is_sufficient:
            print(f"Sorry there is not enough {insufficient_product}.")
        else:
            fee = process_coins()
            if fee < product["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                prepare_product(product, fee)
                print(f"Here is your {product_name}. Enjoy!")

    if command == "cappuccino":
        product_name = "cappuccino"
        product = MENU[product_name]
        if not is_sufficient:
            print(f"Sorry there is not enough {insufficient_product}.")
        else:
            fee = process_coins()
            if fee < product["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                prepare_product(product, fee)
                print(f"Here is your {product_name}. Enjoy!")


    elif command not in ["report", "espresso", "latte", "cappuccino"]:
        print("Invalid command. Please try again.")
