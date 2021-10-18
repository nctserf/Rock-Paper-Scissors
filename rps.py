#20211018:rps.py

#2.1a
"""
This program allows you to play 'rock, paper, scissors' against a computer.
"""

#2.1b
import random

#2.1c
def rps():
    """
    compares user input to randomly generated value and returns outcome of game.
    """
    choice=input("Enter 'rock', 'paper', or 'scissors': ")
    number=random.randint(1,3)
    if number==1:
        if choice=="rock":
            print("tie")
            return "tie"
        elif choice=="paper":
            print("win")
            return "win"
        else:
            print("loss")
            return "loss"
    elif number==2:
        if choice=="rock":
            print("loss")
            return "loss"
        elif choice=="paper":
            print("tie")
            return "tie"
        else:
            print("win")
            return "win"
    else:
        if choice=="rock":
            print("win")
            return "win"
        elif choice=="paper":
            print("loss")
            return "loss"
        else:
            print("tie")
            return "tie"
if __name__=="__main__":
    for i in range(1,6):
        print(i)
        rps()
