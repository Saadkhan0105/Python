print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, L: ")
pepperoni = input("Do you want peooeroni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill += 15
    print("Your Small pizza is ready and your total bill is $15.")    
elif size == "M":
    bill += 20
    print("Child tickets are $5.")
elif size == "L":
    bill += 25
    print("Child tickets are $12.")
else:
    print("You have selected wrong input!")
    

#Pepperoni Choice    
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
    
# Extra Cheese
if extra_cheese == "Y":
    bill += 1



print(f"Your final bill is ${bill}")