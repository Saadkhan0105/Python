user_age = int(input("How old are you? "))

if user_age < 13:
    print("User is Child")
elif user_age < 20:
    print("User is Teenager")
elif user_age < 60:
    print("User is an Adult")
else:
    print("User is Senior")
