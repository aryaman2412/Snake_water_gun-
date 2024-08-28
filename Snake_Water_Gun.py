'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (S for Snake, W for Water, G for Gun): ").upper()
youDict = {"S": 1, "W": -1, "G": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

if youstr in youDict:
    you = youDict[youstr]
    print(f"You Chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw")
    else:
        if computer == -1 and you == 1:
            print("YOU WIN!!")
        elif computer == -1 and you == 0:
            print("YOU LOSE!!")
        elif computer == 1 and you == -1:
            print("YOU LOSE!!")
        elif computer == 1 and you == 0:
            print("YOU WIN!!")
        elif computer == 0 and you == -1:
            print("YOU WIN!!")
        elif computer == 0 and you == 1:
            print("YOU LOSE!!")
else:
    print("Invalid choice! Please enter S, W, or G.")
