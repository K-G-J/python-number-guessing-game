"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():
    name = input("What is your name?  ")

    print(f"Welcome to the number guessing game {name}!")

    answer = random.randint(1, 10)

    def get_guess():
        attempts = 1
        try:
            guess = int(
                input("Try to guess the random number between 1 and 10.  "))
            if guess > 10 or guess < 1:
                attempts += 1
                print(
                    f"{guess} is out of range - the random number is between 1 and 10")
            if guess > answer:
                print("It's lower")
                attempts += 1
                guess = get_guess()
            elif guess < answer:
                print("It's higher")
                attempts += 1
                guess = get_guess()
            else:
                print(
                    f"Got it! 🥳 It took {attempts} attempts to get the correct number")
                print(f"Game over. Thank you for playing {name}")
        except ValueError as err:
            attempts += 1
            print("Oh no! That's not a valid number. Try again...")
            print(f"({err})")
            get_guess()
        else:
            return guess

    get_guess()


start_game()
