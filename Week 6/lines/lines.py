import sys

def line_counter(pythonFile):
    try:
        counter = 0
        with open(pythonFile) as file:
            for line in file:
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                    counter += 1
            return counter
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    


if __name__ == "__main__":
    main()