password = input("Please enter your password: ")
password_length = len(password)

if password_length < 6:
    password_strength = "Weak"
elif password_length <= 10:
    password_strength = "Medium"
else:
    password_strength = "Strong"


print("Your password strentgh is",password_strength)