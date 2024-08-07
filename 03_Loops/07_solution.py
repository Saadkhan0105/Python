# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input('Enter the number between 1 - 10: '))
    if 1 <= number <= 10:
        print(f"The number you have entered is {number} and it is passed")
        break
    else:
        print(f"The number you have entered is {number}. Please enter the number between 1-10")

