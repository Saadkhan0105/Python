# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

uunique_item = set()

for item in items:
    if item in uunique_item:
        print("Duplicate: ", item)
        break
    uunique_item.add(item)