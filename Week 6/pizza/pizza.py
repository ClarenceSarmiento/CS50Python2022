from tabulate import tabulate
import csv
import sys

def to_table(csvFile):
    try:
        with open(csvFile) as file:
            data = csv.reader(file)
            table = tabulate(data, headers= "firstrow", tablefmt= "grid")
            return table
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] == ".csv":
            print(to_table(sys.argv[1]))
        else:
            sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()