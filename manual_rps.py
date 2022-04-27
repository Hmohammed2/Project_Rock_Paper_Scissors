import random as rd


def get_computer_choice():
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = rd.choice(possible_actions)


def get_user_choice():
    possible_actions = ["Rock", "Paper", "Scissors"]
    user_input = input("Enter a choice (rock, paper, scissors): ")
    if user_input in possible_actions:
        print(f"You picked {user_input}")
    else:
        print("You can only pick between Rock, Paper, Scissors")


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"You picked {user_choice} and computer picked {computer_choice}. Its a tie!")
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print("Too bad you lose! Paper beats rock!")
        else:
            print("Well done you win! Rock smashes scissors")
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("Well done you win! Paper beats rock!")
        else:
            print("Too bad you lose! Scissors cuts paper!")
    elif user_choice == "Scissors":
        if computer_choice == "Rock":
            print("Too bad you lose! Rock smashes scissors!")
        else:
            print("Well done you win! Scissors cuts paper!")

if __name__ == '__main__':
    get_user_choice()