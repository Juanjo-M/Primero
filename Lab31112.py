year = int(input("Enter a year: "))
if year >= 1582:
    if year % 4 != 0:
        print("This is a common year.")
    elif year % 100 != 0:
        print("This is a leap year.")
    elif year % 400 != 0:
        print("This is a common year.")
    else:
        print("This is a leap year.")
else:
    print("Not within the Gregorian calendar period")        