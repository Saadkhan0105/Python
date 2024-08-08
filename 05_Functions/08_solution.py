# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwarrgs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwarrgs(name = "Iron-Man", power = "Lazer")
print_kwarrgs(name = "Hulk")
print_kwarrgs(name = "Thor", power = "Mjolnir", enemy = "Thanos")