import random
import sys

def guess(number):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                pass
            else:
                if guess < number:
                    print("Too small!")
                elif guess > number:
                    print("Too large!")
                else:
                    print("Just right!")
                    sys.exit()
        except ValueError:
            pass
        except EOFError:
            print()
            break

def main():
    while True:
        try:
            level = int(input("Level: "))
            number = random.randint(1, level)
            guess(number)
        except ValueError:
            pass
        except EOFError:
            print()
            break

main()