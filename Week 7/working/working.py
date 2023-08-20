import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Time input format (12:00 AM or 12 AM)
    time_format = "(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    # 9:00 AM to 5:00 PM or 9 AM to 5 PM
    time = r"^" + time_format + " to " + time_format + "$"
    if matches := re.search(time, s):
        format_12 = reformat(matches.group(1), matches.group(2), matches.group(3))
        format_24 = reformat(matches.group(4), matches.group(5), matches.group(6))
        return f"{format_12} to {format_24}"
    else:
        raise ValueError

def reformat(HH, MM, XM): # Function to reformat 12 hour to 24 hour format
    # Sample: 9:00 AM to 5:00 PM = 09:00 to 17:00
    if HH == "12":
        if XM == "AM":
            hr = "00"
        else:
            hr = "12"
    else:
        if XM == "AM":
            hr = f"{int(HH):02}"
        else:
            hr = f"{int(HH) + 12}"
    if MM == None:
        min = "00"
    else:
        min = f"{int(MM):02}"

    return f"{hr}:{min}"


if __name__ == "__main__":
    main()