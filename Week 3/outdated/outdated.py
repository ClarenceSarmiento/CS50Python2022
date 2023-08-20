months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

def convert(months):
    while True:
        input_date = input("Date: ")
        try:
            if "/" in input_date:
                month, date, year = input_date.split("/")
            elif "," in input_date:
                month_date, year = input_date.split(",")
                month, date = month_date.split(" ")
                month = months.index(month) + 1
            if int(month) > 12 or int(date) > 31:
                raise ValueError
        except (KeyError, ValueError, NameError):
            pass
        else:
            print(f"{int(year)}-{int(month):02}-{int(date):02}")
            break

convert(months)