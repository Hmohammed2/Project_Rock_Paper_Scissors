import random as rd


def get_computer_choice():
    # function simulates a computer choosing between rock, paper and scissors
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = rd.choice(possible_actions)
    return computer_action


def get_user_choice():
    # Function gets user choice
    possible_actions = ["rock", "paper", "scissors"]
    user_input = input("Enter a choice (rock, paper, scissors): ")
    if user_input in possible_actions:
        print(f"You picked {user_input}")
    else:
        print("You can only pick between Rock, Paper, Scissors")
    return user_input


def get_winner(user_choice, computer_choice):
    print(f"Computer picks {computer_choice}")
    if user_choice == computer_choice:
        print(f"You picked {user_choice} and computer picked {computer_choice}. Its a tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("Too bad you lose! Paper beats rock!")
        else:
            print("Well done you win! Rock smashes scissors")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Well done you win! Paper beats rock!")
        else:
            print("Too bad you lose! Scissors cuts paper!")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("Too bad you lose! Rock smashes scissors!")
        else:
            print("Well done you win! Scissors cuts paper!")


def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(user_choice, computer_choice)


if __name__ == '__main__':
    play()