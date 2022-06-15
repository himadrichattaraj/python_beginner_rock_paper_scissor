# play rock paper scissor with computer
import random

choices = ["rock", "paper", "scissor"]
computer = random.choice(choices)
while True:
    player = ""
    while player not in choices:
        player = input("rock, paper or scissor?: ").lower()
        if player not in choices:
            print("Check your spelling!")
    print("Computer: " + computer)
    print("Player: " + player)
    if player == choices[0] and computer == choices[1] or player == choices[1] and computer == choices[2] or player == \
            choices[2] and computer == choices[0]:
        print("You Lose!")
    elif computer == choices[0] and player == choices[1] or computer == choices[1] and player == choices[
        2] or computer == choices[2] and player == choices[0]:
        print("You Win!")
    else:
        print("Tie! Try Again")
    while True:
        play = input("Wanna Play Again? ").lower()
        if play == "yes":
            break
        elif play == "no":
            break
        else:
            print("Please enter only yes or no.")
    if play == "no":
        break
print("Bye!!")
