
#Number Guessing Game Using Loops and conditional statements
# This will help to Import the random module that pick a secret number

import random

def guess():

# Generate a random number between 0 and 100
    ans = random.randint(0, 100)

# Start a loop
    while True:
# Take user input to guess a number

        ges = int(input("Guess any number: "))

# Check if user guess is correct 

        if ges == ans:
            print(f"{ges} Your guess is correct!")
            break

# If guess is too low
        elif ges < ans:
            print(f"{ges} Your guess is too low")

# If guess is too high
        else:
            print(f"{ges} Your guess is too high")

# Call function to play the game
guess()

