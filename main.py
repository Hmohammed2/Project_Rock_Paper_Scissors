from cv2 import cv2
from keras.models import load_model
import numpy as np
import random as rd

player_score = 0
computer_score = 0


class Game:
    def __init__(self):
        # Constructor
        self.possible_actions = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        # method simulates a computer choosing between rock, paper and scissors
        computer_action = rd.choice(self.possible_actions)
        return computer_action

    def get_user_choice(self, user_choice):
        # Method gets user choice
        if user_choice in self.possible_actions:
            print(f"You picked {user_choice}")
        else:
            print("You can only pick between Rock, Paper, Scissors")
            raise KeyError
        return user_choice

    def get_winner(self, user_choice):
        global player_score, computer_score

        computer_choice = self.get_computer_choice()

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


model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
game = Game() # Initialise game class
counter = 70

while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    max_value = np.where(prediction == np.amax(prediction))
    # pulls out the max probability value and locates the index which it is located in. THe index represents the label
    # 0 label is rock, 1 label is scissors, 2 label is paper, 3 label is nothing


    def prediction_output(max_val): # function gets the max value from the multidimensional array and returns the
        # gesture
        if max_val[1] == 0:
            users_choice = "rock"
        elif max_val[1] == 1:
            users_choice = "scissors"
        elif max_val[1] == 2:
            users_choice = "paper"
        else:
            users_choice = "nothing"
        return users_choice


    # counter variable which counts to 0 and initiates the users most probable hand gesture
    counter = counter - 1

    if counter == 0:
        player_choice = prediction_output(max_value)
        print(player_choice)
        game.get_winner(player_choice)
        print(f"Player: {player_score}")
        print(f"Computer: {computer_score}")
        counter = 70

    if player_score or computer_score == 3:
        play_again = input("Play again? (y/n)")
        if play_again.lower() != "y":
            break
        else:
            player_score = 0
            computer_score = 0

    # Press q to close the window
    # print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #    play_again = input("Play again (y/n)")
    #    if play_again.lower() != "y":
    #        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()