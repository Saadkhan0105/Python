#Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Please enter your birth year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"Your birth year, {year} is a leap year.")
else:
    print(f"Your birth year, {year} is not a leap year.")
