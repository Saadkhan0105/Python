#Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = input('Enter the color: ')

if fruit == "Banana":
    if color == "Green":
        print("Fruit is Unripe")
    elif color == "Yellow":
        print("Fruit is Ripe")
    elif color == "Brown":
        print("Fruit is Overripe")
