from datetime import date
import inflect
import operator
import sys

p = inflect.engine()


def main():
    try:
        date_of_birth = date.fromisoformat(input("Date of Birth (YYYY-MM-DD): "))
        today = date.today()
        difference = operator.sub(today, date_of_birth)
        print(day_to_minutes(difference.days))
    except ValueError:
        sys.exit("Invalid date")


def day_to_minutes(day):
    minutes = day * 24 * 60
    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"


if __name__ == "__main__":
    main()