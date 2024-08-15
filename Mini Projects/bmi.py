weight = int(input("Please enter your weight: "))
height = float(input("Please enter your height: "))

bmi = weight / (height ** 2)
bmi = round(bmi, 2)

if bmi < 18.5:
    print("You are Underweight!")
elif 18.5 <= bmi < 25:
    print("Your weight is Normal!")
else:
    print("You are Overweight")

print("Your BMI score is: " ,bmi)