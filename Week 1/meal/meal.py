def main():
    time = input("What time is it? ").strip()
    """ Check if the time is in given range:
    7:00 - 8:00 : Breakfast
    12:00 - 13:00 : Lunch
    18:00 - 19:00 : Dinner """
    if 7.00 <= convert(time) <= 8.00:
        print("breakfast time")
    elif 12.00 <= convert(time) <= 13.00:
        print("lunch time")
    elif 18.00 <= convert(time) <= 19.00:
        print("dinner time")
    else:
        return


def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    # Convert minute to hour using minute x 1 hour / 60 minutes
    minute = float(minute) * 1 / 60
    converted = hour + minute
    return converted

if __name__ == "__main__":
    main()