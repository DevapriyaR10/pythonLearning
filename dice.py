import random

again=True

while again:
    print(random.randint(1, 6))
    again_roll=input("Do you want to roll the dice again? (y/n)")
    if again_roll.lower()=='y':
        continue
    else:
        break