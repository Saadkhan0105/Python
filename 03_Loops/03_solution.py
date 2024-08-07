# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Enter the table you want to print: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(number, 'x', i, '=', number * i)