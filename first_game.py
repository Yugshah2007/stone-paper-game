# stone paper secessor game

import random

game = {1: "stone", 0: "paper", -1: "secessor"}

while True:
    computer = random.choice([-1, 0, 1])
    prins = game[computer]
    print(f"computer chose: {prins}")

    you = int(input("enter -1, 0, or 1: "))

    if you not in (-1, 0, 1):
        print("game exited you entered something wrong")
        break

    priwt = game[you]

    if prins == priwt:
        print("game draw")
    else:
        if computer == -1 and you == 0:
            print("you lose!")
        elif computer == -1 and you == 1:
            print("you lose!")
        elif computer == 0 and you == -1:
            print("you win!")
        elif computer == 0 and you == 1:
            print("you lose!")
        elif computer == 1 and you == 0:
            print("you won!")
        elif computer == 1 and you == -1:
            print("you lose!")
        else:
            print("something went wrong!!!")
