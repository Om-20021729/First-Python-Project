'''
🎯 Project: Snake, Water, Gun Game (Python)
This is a simple Python game where the user plays against the computer.
✔ Snake beats Water (Snake drinks Water 🐍💧)
✔ Water beats Gun (Water rusts the Gun 💧🔫)
✔ Gun beats Snake (Gun kills Snake 🔫🐍)

1 for snake
-1 for water
0 for gun

'''
import random

computer = random.choice([-1, 0, 1])

youstr =  input("Enter your choice:  ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

# By now we have 2 numbers, you and computer


print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if(computer == you):
    print("its a Draw 🫂🫂")

else: 
    if(computer == -1 and you == 1):
       print("You win!🙂🙂")

    elif(computer == -1 and you == 0):  
       print("You Lose 🙄🙄")

    elif(computer == 1 and you == -1):  
       print("You Lose 🙄🙄")

    elif(computer == 1 and you == 0):  
       print("You win!🙂🙂")

    elif(computer == 0 and you == -1):  
       print("You Win!🙂🙂")

    elif(computer == 0 and you == 1):  
       print("You Lose 🙄🙄")

    else:
       print("Something went wrong 🥴🥴")