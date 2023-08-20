def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent))

def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if (x/y) > 1:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError

    return round(x / y * 100)

def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif 1 < percentage < 99:
        return f"{percentage}%"

if __name__ == "__main__":
    main()