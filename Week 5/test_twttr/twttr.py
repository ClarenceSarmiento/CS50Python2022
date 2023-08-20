def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(word):
    new_word = ""
    vowels = ["a", "e", "i", "o", "u",
              "A", "E", "I", "O", "U"]
    for letter in word:
        if letter not in vowels:
            new_word += letter
    return new_word

if __name__ == "__main__":
    main()