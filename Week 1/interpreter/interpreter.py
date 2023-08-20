expression = input("Expression: ").strip()
num1, symbol, num2 = expression.split(" ")

num1 = int(num1)
num2 = int(num2)

match symbol:
    case "+":
        result = float(num1 + num2)
        print(f"{result:.1f}")
    case "-":
        result = float(num1 - num2)
        print(f"{result:.1f}")
    case "*":
        result = float(num1 * num2)
        print(f"{result:.1f}")
    case "/":
        result = float(num1 / num2)
        print(f"{result:.1f}")