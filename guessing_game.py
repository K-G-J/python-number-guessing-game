"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

answer = random.randint(1, 10)

attempts = 0

name = input("What is your name?  ")

print(f"Welcome to the number guessing game {name}! 😄")


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
