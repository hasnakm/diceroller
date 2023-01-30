import random

again = True

while again:
    n=random.randint(1,6)
    if n==1:
        print("┌─────────┐")
        print("│         │")
        print("│    ●    │")
        print("│         │")
        print("└─────────┘")
    elif n==2:
        print("┌─────────┐")
        print("│  ●      │")
        print("│         │")
        print("│      ●  │")
        print("└─────────┘")
    elif n==3:
        print("┌─────────┐")
        print("│  ●      │")
        print("│    ●    │")
        print("│      ●  │")
        print("└─────────┘")
    
    elif n==4:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│         │")
        print("│  ●   ●  │")
        print("└─────────┘")
    elif n==5:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│    ●    │")
        print("│  ●   ●  │")
        print("└─────────┘")
    else:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("└─────────┘")

    another_roll=input("Want to roll the dice again? (y/n) : ")
    if another_roll.lower()=="y":
        continue
    else:
        break
