# Problem: Check if a number is prime.

number = int(input("Please enter the number: "))

is_Prime = True

if number > 1:
    for i in range(2, number + 1):
        if (number % i) == 0:
            is_Prime = False
            break

print(number, "It is a Prime Number.")