from cv2 import cv2
from keras.models import load_model
import numpy as np


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
        computer_choice = self.get_computer_choice()

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


model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
game = Game()
counter = 10

while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    max_value = np.where(prediction == np.amax(prediction))


    def prediction_output(max_val):
        if max_val[1] == 0:
            user_choice = "rock"
        elif max_val[1] == 1:
            user_choice = "scissors"
        elif max_val[1] == 2:
            user_choice = "paper"
        else:
            user_choice = "nothing"
        return user_choice


    # counter variable which counts to 0 and initiates the users hand gesture
    counter = counter - 1
    print(counter)

    if counter == 0:
        print(prediction_output(max_value))
        counter = 10

    # Press q to close the window
    # print(prediction)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()