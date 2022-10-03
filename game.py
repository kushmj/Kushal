# import random module
import random

while True:
    choices = ['rock','paper', 'scissor']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Enter your choice (rock, paper, scissor) : ").lower()

    if player == computer:

        print("player choice:", player)
        print("computer choice:", computer)
        print(player + " vs " + computer)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("player choice:", player)
            print("computer choice:", computer)
            print(player + " vs " + computer)
            print("you lose!")
        if computer == "scissor":
            print("player choice:", player)
            print("computer choice:", computer)
            print(player + " vs " + computer)
            print("you win!")

    elif player == "scissor":
        if computer == "rock":
            print("player choice:", player)
            print("computer choice:", computer)
            print(player + " vs " + computer)
            print("you lose!")
        if computer == "paper":
            print("player choice:", player)
            print("computer choice:", computer)
            print(player + " vs " + computer)
            print("you win!")

    elif player == "paper":
        if computer == "scissor":
            print("player choice:", player)
            print("computer choice:", computer)
            print(player + " vs " + computer)
            print("you lose!")
        if computer == "rock":
            print("player choice:", player)
            print("computer choice:", computer)
            print(player + " vs " + computer)
            print("you win!")

    play_again = input("do you want to play again? (y/n)").lower()


    if play_again == "n":
        break

print("Thank you for playing")
