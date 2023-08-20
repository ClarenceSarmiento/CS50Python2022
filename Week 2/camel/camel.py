camelCase = str(input("camelCase: "))
print("snake_case: ", end="")
for letter in camelCase:
    if letter.islower():
        print(letter, end="")
    else:
        print("_" + letter.lower(), end="")

print()