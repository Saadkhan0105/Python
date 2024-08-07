# Problem: Reverse a string using a loop

input_str = "A man, a plan, a canal – Panama"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str

print(reversed_str)