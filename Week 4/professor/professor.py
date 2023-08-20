import random

def main():
    # 10 math problems
    problems = 10
    # 3 tries
    lives = 3
    # user's score based on correct answers
    correct_answers = 0
    # get user's level
    level = get_level()

    while problems != 0:
        # Generate random problem
        if lives == 3:
            x, y = generate_integer(level)
        try:
            answer = int(input(f"{x} + {y} = "))
            result = x + y
            if answer == result:
                problems -= 1
                correct_answers += 1
                lives = 3
                continue
            else:
                raise ValueError
        except (NameError, ValueError): # If an answer is not correct (or not even a number),
            # the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
            print("EEE")
            lives -= 1
            pass
        # If the user has still not answered correctly after three tries, the program should output the correct answer.
        if lives == 0:
            print(f"{x} + {y} = {result}")
            lives = 3 # reset user's lives for new problem
            problems -= 1
            continue
    print(f"Score: {correct_answers}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif level == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    elif level == 3:
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)
    return num1, num2

if __name__ == "__main__":
    main()