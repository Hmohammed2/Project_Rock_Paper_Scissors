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


if __name__ == '__main__':
    get_user_choice()