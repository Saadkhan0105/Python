year = int(input("Please enter your birth year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"Your birth year, {year} is a leap year.")
else:
    print(f"Your birth year, {year} is not a leap year.")