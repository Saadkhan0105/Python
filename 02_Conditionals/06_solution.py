Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

Distance = int(input("What is the distance that you would likely travel? "))

if Distance <=3:
    transportation = "You should prefer Walking"
elif Distance <=15:
    transportation = "You should travel by  Bike"
else:
    transportation = "You should travel by Car"

print("AI recommends:", transportation)
