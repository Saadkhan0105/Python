# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return round(area, 2), round(circumference, 2)

a, c = circle_stats(int(input("Enter the radius: ")))
print("Area: {:.2f}, Circumference: {:.2f}".format(a, c))
