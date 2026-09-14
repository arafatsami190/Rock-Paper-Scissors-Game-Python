import random

player_choice = input("Enter your choice (rock, paper, scissors): ")
computer_choice = random.choice(['rock', 'paper', 'scissors'])

choices_dictionary = {"player": player_choice, "computer": computer_choice}

def choices(player, computer):
    print(f"You chose {player}, computer chose {computer}.")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "paper":
        print("Paper covers the rock. you lose!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("Rock smashes the scissors. You win!")
    elif player_choice == "paper" and computer_choice == "scissors":
        print("Scissors cut the paper. you lose!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("Paper covers the rock. you win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Scissors cut the paper. you win!")
    elif player_choice == "scissors" and computer_choice == "rock":
        print("rock smashes the scissors. you lose!")
    else:
        print("ERORR!")

choices(player_choice, computer_choice)
