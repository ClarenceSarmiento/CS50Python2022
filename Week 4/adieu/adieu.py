import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").title()
        names.append(name)
    except EOFError:
        print()
        print("Adieu, adieu, to", p.join(names))
        break