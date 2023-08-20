query = input("What is the Answer to the Great Question of Life, Universe, and Everything? ").lower().strip()

match query:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")

