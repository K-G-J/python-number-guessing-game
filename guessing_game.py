"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

name = input("What is your name?  ")

print(f"Welcome to the number guessing game {name}! 😄")

answer = random.randint(1, 10)

attempts = 0


def get_guess():
    global attempts
    attempts += 1
    try:
        guess = int(
            input("Try to guess the random number between 1 and 10.  "))
        if guess > 10 or guess < 1:
            print(
                f"{guess} is out of range 😕 the random number is between 1 and 10")
        if guess > answer:
            print("It's lower ⬇")
            get_guess()
        elif guess < answer:
            print("It's higher ⬆")
            get_guess()
        else:
            print(
                f"Got it! 🥳 \n It took {attempts} attempts to get the correct number \n Game over 👋. \n Thank you for playing {name} 😄")
    except ValueError as err:
        print("Oh no! That's not a valid number 😕. Try again...")
        print(f"({err})")
        get_guess()
    else:
        return guess


def start_game():

    get_guess()


start_game()

"""
Extra Credit
To get an "exceeds" rating, complete all of the steps below:

4 steps
    1.  As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again. For example, if the range is 1-10 and the player enters 12 they should be informed that this number is outside the range.
    2.  As a player of the game, after I guess correctly I should be prompted if I would like to play again.
    3.  As a player of the game, at the start of each game I should be shown the current high score (least amount of points) so that I know what I am supposed to beat.
    4.  Every time a player decides to play again, the random number to guess is updated so players are guessing something new each time.
"""
