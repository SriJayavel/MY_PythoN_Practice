import random

while True:
    computer = random.choice(["rock", "paper", "scissors"])
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Player chooses rock, paper, or scissors?: ")

    if player == computer:
        print("Computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ",computer)
            print("player: ",player)
            print("You lost!")
        if computer == "scissors":
            print("Computer: ",computer)
            print("player: ",player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: ",computer)
            print("player: ",player)
            print("You lost!")
        if computer == "rock":
            print("Computer: ",computer)
            print("player: ",player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer: ",computer)
            print("player: ",player)
            print("You lost!")
        if computer == "paper":
            print("Computer: ",computer)
            print("player: ",player)
            print("You win!")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes":
        break
print("Thanks for playing!")

