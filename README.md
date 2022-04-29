# Computer Vision Rock Paper Scissors
This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

## Table of contents
* [Technologies](#technologies)
* [Milestone 1: Creating the Model](#Milestone-1:-Creating-the-Model)
* [Milestone 2: Installing the dependencies](Milestone-2)
* [Milestone 3: Creating the Rock, Paper Scissors Game](#milestone-3)

## Technologies
* Pycharm 
* Teachable Machines

## Milestone 1: Creating the Model
FIrst an image project model is created with 4 classes being: Rock, Paper, Scissors & Nothing. 

This was done using the web based tool "Teachable Machines". Teachable Machine is a web-based tool that makes creating machine learning models fast, easy, and accessible to everyone. 

Firstly, you would have to process the images of the 4 options using either a webcam or a photo that has already been uploaded in a suitable file location. By using more image samples, this would improve the accuracy of the model.
After the tool has trained the model, it is then downloaded and exported into a keras.h5 model to be used in the python code.

## Milestone 2: Installing the dependencies
Create an environment and then install the necessary requirements. You need, at least, opencv-python, tensorflow, and ipykernel. 

Pycharm was used for this. Once the environment is setup, the model that was downloaded previously is ran on pycharm. Code is within the python file "Rock, Paper Scissors.py"

## Milestone 3: Creating the Rock, Paper Scissors Game
This code needs to randomly choose an option (rock, paper, or scissors), and then ask the user for an input.

This was created in another file called manual_rps.py that will be used to play the game without the camera.

The random module was imported to pick a random option between rock, paper, and scissors and the input function to get the user's choice.

Two functions was created being: get_computer_choice and get_user_choice. The first function will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice. The second function will ask the user for an input and return it.

Using if-elif-else statements, the script should now choose a winner based on the classic rules of Rock-Paper-Scissors. For example, if the computer chooses rock and the user chooses scissors, the computer wins.

The code was wrapped in a function called get_winner which returned the winner. This function takes two arguments: computer_choice and user_choice. Finally, a new function was created called "play". Inside the function all the three functions that were created are then called (get_computer_choice, get_user_choice, and get_winner).

## Milestone 4: Using the Camera to play RPS



