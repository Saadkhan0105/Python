#Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("Enter your pet specie: ")
year = int(input("How old is your Pet? "))

if species == "Dog":
    if year < 2:
        food = "Puppy Food"
    elif year <= 7:
        food = "Adult dog food"
    else:
        food = "Senior dog food"

elif species == "Cat":
    if year < 2:
        food = "Kitten Food"
    elif year <= 7:
        food = "Adult Cat Food"
    else:
        food = "Senior Cat Food"

print(f"Your Pet is {species} and the age of pet is {year} years and the recommended food is", food)
