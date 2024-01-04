import random
options=("rock", "paper", "scissors")
player=None

computer=random.choice(options)
game=True
while game:
    while player not in options:   
        player=input("Enter a choice (rock, paper, scissors): ")

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player==computer:
            print("Its a tie!")

        elif player=="rock" and computer=="scissors":
            print("You won!")

        elif player=="scissors" and computer=="paper":
            print("You won!")
            
        elif player=="paper" and computer=="rock":
            print("You won!")
            
        else:
            print("You lost :'(")
        again=input("Do you want to continue? (y/n)")
        if again.lower()=='n':
            game=False
            