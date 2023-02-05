"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import sys


def get_guess(attempts, answer, name):
    while True:
        try:
            attempts += 1
            guess = int(
                input("Try to guess the random number between 1 and 10.  "))
            if guess > 10 or guess < 1:
                # Handle out of range guesses
                print(
                    f"{guess} is out of range 😕 the random number is between 1 and 10")
            elif guess > answer:
                print("It's lower ⬇")
            elif guess < answer:
                print("It's higher ⬆")
            elif guess == answer:
                # Handle correct guess
                print(
                    f"Got it! 🥳 \n It took {attempts} attempt{'' if attempts == 1 else 's'} to get the correct number \n Game over 👋. \n Thank you for playing {name} 😄")
                return attempts
            else:
                print("Oops 😕 ... something went wrong. Please try again.")
        except ValueError as err:
            # Handle invalid input guesses
            print("Oh no! That's not a valid number 😕. Try again...")
            print(f"({err})")


def start_game(name):
    # Reset attempts and new random number before each round
    attempts = 0
    answer = random.randint(1, 10)

    return get_guess(attempts, answer, name)


def main():
    high_score = 0

    name = input("What is your name?  ")
    print(f"Welcome to the number guessing game {name}! 😄")
    attempts = start_game(name)

    while True:
        # Set and display high score
        if high_score == 0 or attempts < high_score:
            high_score = attempts
            print("You set the high score! 🤩")

        if high_score != 0:
            print(f"The current high score is {high_score} 🤗")

        # Prompt player if they would like to replay
        replay_choice = (input("Would you like to play again? Y/N?  ")).lower()
        if replay_choice == "y":
            attempts = start_game(name)
        elif replay_choice == "n":
            sys.exit(
                f"Thank you for playing the random number guessing game {name} 😸")
        else:
            # Handle invalid input
            print('Oops 😕 ... please enter either "Y" or "N"')


if __name__ == "__main__":
    main()
