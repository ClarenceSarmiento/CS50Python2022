amount_due = 50
change = 0
denominations = [25, 10, 5]

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    paid = int(input("Insert Coin: " ))
    if paid in denominations:
        amount_due -= paid
        change += paid

if change >= amount_due:
    print(f"Change Owed: {change - 50}")

