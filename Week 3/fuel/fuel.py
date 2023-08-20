def fraction_to_percent(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            result = int(x)/int(y) * 100
            if 10 >= result >= 0:
                return "E"
            elif 100 >= result >= 90:
                return "F"
            elif 90 > result > 10:
                return str(round(result)) + "%"
        except (ValueError, ZeroDivisionError):
            pass

def main():
    fuel_fraction = fraction_to_percent("Fraction: ")
    print(fuel_fraction)

main()