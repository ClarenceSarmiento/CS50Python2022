vowels = ["a", "e", "i", "o", "u",
          "A", "E", "I", "O", "U"]

text = str(input("Input: "))
print("Output: ", end="")

for letter in text:
    if letter not in vowels:
        print(letter, end="")

print()