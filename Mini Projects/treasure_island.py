print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
      ''')

print("Welcome to Treasure Island! Your mission to find the treasure")

choice1= input('You\'re at a cross road. Where do want to go: | Type "left" or "right" .\n').lower()

if choice1 == "left":
    chocie2 = input('You\'ve come to a lake. There is an island in the middle of the lake | Type "wait" to wait for a boat. Type "swim" to swim accross \n')

    if chocie2 == "wait":
        choice3 = input("You have arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
            print("It is a room full of fire🔥")
        elif choice3 == "yellow":
            print("Congratulations you have found the Treasure. 🎉")
        elif choice3 == "blue":
            print("It is a room full of beast🦍")
        else:
            print("You chose a door that does not exist. Game Over.")
    else:
        print("You have been Attacked by trout. Game Over.")



else:
    print("You have fell into a hole. Game Over")
