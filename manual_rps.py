import random as rd


player_score = 0
computer_score = 0


class Action:
    def __init__(self):
        self.rock = 0
        self.paper = 1
        self.scissors = 2
        self.nothing = 3


class Game:

    def __init__(self):
        # Constructor
        self.possible_actions = ["rock", "paper", "scissors"]
        self.user_choice = input("Enter a choice (rock, paper, scissors): ")

    def get_computer_choice(self):
        # method simulates a computer choosing between rock, paper and scissors
        computer_action = rd.choice(self.possible_actions)
        return computer_action

    def get_user_choice(self):
        # Method gets user choice
        if self.user_choice in self.possible_actions:
            print(f"You picked {self.user_choice}")
        else:
            print("You can only pick between Rock, Paper, Scissors")
            raise KeyError
        return self.user_choice

    def get_winner(self):
        global player_score, computer_score

        computer_choice = self.get_computer_choice()
        user_choice = self.user_choice

        print(f"Computer picks {computer_choice}")

        if user_choice == computer_choice:
            print(f"You picked {user_choice} and computer picked {computer_choice}. Its a tie!")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Too bad you lose! Paper beats rock!")
                computer_score += 1
            else:
                print("Well done you win! Rock smashes scissors")
                player_score += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Well done you win! Paper beats rock!")
                player_score += 1
            else:
                print("Too bad you lose! Scissors cuts paper!")
                computer_score += 1
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Too bad you lose! Rock smashes scissors!")
                computer_score += 1
            else:
                print("Well done you win! Scissors cuts paper!")
                player_score += 1


def play():
    global player_score, computer_score
    while True:
        game = Game()
        game.get_winner()
        print(f"Player: {player_score}")
        print(f"Computer: {computer_score}")
        if player_score == 3 or computer_score == 3:
            if player_score == 3:
                print("Well done you beat the computer!")

            else:
                print("Aww you lost! Better luck next time")
            player_score = 0
            computer_score = 0
            play_again = input("Play again (y/n)")
            if play_again.lower() != "y":
                break


def test():
    app = Action()
    print(dir(app))
    print(app.__dict__)


if __name__ == '__main__':
    play()
