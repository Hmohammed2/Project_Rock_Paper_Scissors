# Computer Vision Rock Paper Scissors
This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

## Table of contents
* [Technologies](#technologies)
* [Milestone 1: Creating the Model](#Milestone-1-Creating-the-Model)
* [Milestone 2: Installing the dependencies](#Milestone-2-Installing-the-dependencies)
* [Milestone 3: Creating the Rock, Paper Scissors Game]([#Milestone-3-Creating-the-Rock-Paper-Scissors-Game)
* [Milestone 4: Using the Camera to play RPS]([#Milestone-4-Using-the-Camera-to-play-RPS)
* [Conclusion](#Conclusion)

## Technologies
* Pycharm 
* Teachable Machines
* Webcam

## Milestone 1: Creating the Model
- FIrst an image project model is created with 4 classes being: Rock, Paper, Scissors & Nothing. 

- This was done using the web based tool "Teachable Machines". Teachable Machine is a web-based tool that makes creating machine learning models fast, easy, and accessible to everyone. 

- Firstly, you would have to process the images of the 4 options using either a webcam or a photo that has already been uploaded in a suitable file location. By using more image samples, this would improve the accuracy of the model.
After the tool has trained the model, it is then downloaded and exported into a keras.h5 model to be used in the python code.

## Milestone 2: Installing the dependencies
- Create an environment and then install the necessary requirements. You need, at least, opencv-python, tensorflow, and ipykernel. 

- Pycharm was used for this. Once the environment is setup, the model that was downloaded previously is ran on pycharm. Code is within the python file "Rock, Paper Scissors.py"

## Milestone 3: Creating the Rock, Paper Scissors Game
- This code needs to randomly choose an option (rock, paper, or scissors), and then ask the user for an input.

- This was created in another file called manual_rps.py that will be used to play the game without the camera.

- The random module is imported which will be used to simulate the computers choice. THe code will be encapsulated in the class labelled "Game". THe constructor will be the three choices "Rock", "Paper", "scissors". It will also initialise the user input variable to allow the user to pick their option

```python
import random as rd

class Game:

    def __init__(self):
        # Constructor
        self.possible_actions = ["rock", "paper", "scissors"]
        self.user_choice = input("Enter a choice (rock, paper, scissors): ")
        
```
- Two methods were created being: "get_computer_choic" and "get_user_choice". The first method will be the computers_choice and will randomly pick an option between "Rock", "Paper", and "Scissors". The second function will store users input.

```python

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
        return user_choice 

```
- Using if-elif-else statements, the script should now choose a winner based on the classic rules of Rock-Paper-Scissors. For example, if the computer chooses rock and the user chooses scissors, the computer wins.

- The code was wrapped in a method called get_winner which returns the winner. This method utlises both the: computer_choice and user_choice method. Finally, a new function was created called "play". Inside the function, the Game class is initalised and the "get_winner" method is called which also links to the other two methods. (get_computer_choice, get_user_choice, and get_winner).

```python
    def get_winner(self):

        computer_choice = self.get_computer_choice()
        user_choice = self.user_choice

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
    while True:
        game = Game()
        game.get_winner()

```
## Milestone 4: Using the Camera to play RPS

- The code that used the webcam is then combined with the function that asks the user for an input, found in the manual game done previously.
However, now the manual input will need to be replaced for the output of the computer vision model.

```python
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
game = Game()  # Initialise game class

while True:

    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
```

- The output of the model downloaded represents a list of probabilities for each class. The output of the vision model will need to pick the class with the highest probability. THis was done using the numpy function numpy.amax() to find the index which corresponds to the max value. This is then stored the variable "max_value"

```python
max_value = np.where(prediction == np.amax(prediction))
```
- So, assuming the model trained has labels in this order: "Rock", "Paper", "Scissors", and "Nothing". If the first element of the list is 0.9, the second element is 0.1, the third element is 0.05, and the fourth element is 0.05, then, the model predicts that you showed "Rock" to the camera.

An extra functionality was also implemented to have a countdown timer to show the user when the user should show their gesture by. 
```python
    countdown = 80  # Timer until game starts
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, str(countdown),  # Puts in a countdown timer to let user know when to input hand gesture
                (200, 250), font,
                7, (0, 255, 255),
                4, cv2.LINE_AA)
    countdown = countdown - 1  # countdown variable which counts to 0 and initiates the users most probable hand gesture
```

- Finally, the function "score_system" was added to store the user and computers scores. If either the computer or the user wins three rounds the game ends, with the option for the user to play the game again via input (Y/N).

```python
 def score_system():  # function stores the score
        global player_score, computer_score

        player_choice = prediction_output(max_value)
        print(f"You picked {player_choice}")
        game.get_winner(player_choice)
        print(f"Player: {player_score}")
        print(f"Computer: {computer_score}")


    if countdown == 0:
        score_system()
        countdown = 80  # restart the counter
    if player_score == 3 or computer_score == 3:
        if player_score == 3:
            print("Well done you beat the computer!")
        else:
            print("Aww you lost! Better luck next time")
        play_again = input("Play again? (Y/n)")
        if play_again.lower() != "y":
            break
        else:
            player_score = 0
            computer_score = 0
```
## Conclusion
- 
