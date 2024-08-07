#Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).


weather = input("How is the weather today? ")

if weather == "Sunny":
    activity = "Let's go for a Walk"
elif weather == "Rainy":
    activity = "Read a Book"
elif weather == "Snowy":
    activity = "Build a Snowman"

print(activity)
