"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():
    name = input("What is your name?  ")

    print(f"Welcome to the number guessing game {name}!")

    answer = random.randint(1, 100)

    attempts = 1

    def get_guess():
        try:
            guess = int(
                input("Try to guess the random number between 1 and 100.  "))
            if guess > 100 or guess < 1:
                raise ValueError(
                    "Out of range - the random number is between 1 and 100")
            return guess
        except ValueError as err:
            print("Oh no! That's not a valid number. Try again...")
            print(f"({err})")
            get_guess()

    guess = get_guess()

    while guess != answer:
        attempts += 1
        if guess > answer:
            print("It's lower")
            guess = get_guess()
        if guess < answer:
            print("It's higher")
            guess = get_guess()

    print(f"Got it! 🥳 It took {attempts} attempts to get the correct number")
    print(f"Game over. Thank you for playing {name}")


start_game()
