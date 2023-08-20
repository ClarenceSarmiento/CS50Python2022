menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# updates when foods are added
overall_price = 0

while True:
    try:
        food = input("Item: ").title().strip()
        overall_price += menu[food]
        print(f"Total: ${overall_price:.2f}")
    # Catch KeyError if the food is not on the menu
    except KeyError:
        pass
    # detect when the user has inputted control-d by catching an EOFError
    except EOFError:
        print()
        break