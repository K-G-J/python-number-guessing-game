"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import sys

high_score = 0

def get_guess(attempts, answer, name):
    global high_score
    while True:
        try:
            attempts += 1
            guess = int(
                input("Try to guess the random number between 1 and 10.  "))
            if guess > 10 or guess < 1:
                # Handle out of range guesses
                print(
                    f"{guess} is out of range 😕 the random number is between 1 and 10")
                continue
            elif guess > answer:
                print("It's lower ⬇")
                continue
            elif guess < answer:
                print("It's higher ⬆")
                continue
            elif guess == answer:
                # Handle correct guess
                print(
                    f"Got it! 🥳 \n It took {attempts} attempt to get the correct number \n Game over 👋. \n Thank you for playing {name} 😄") if attempts == 1 else print(
                    f"Got it! 🥳 \n It took {attempts} attempts to get the correct number \n Game over 👋. \n Thank you for playing {name} 😄")
                # Save and update high_score
                if high_score == 0 or attempts < high_score:
                    high_score = attempts
                    print("You set the high score! 🤩")
                break
            else:
                print("Oops 😕 ... something went wrong. Please try again.")
                continue
        except ValueError as err:
            # Handle invalid value guesses
            print("Oh no! That's not a valid number 😕. Try again...")
            print(f"({err})")
            continue


def start_game(name):
    global high_score
    # Display current high score
    if high_score != 0:
        print(f"The current high score is {high_score} 🤗")
    # Reset attempts and new random number before each round
    attempts = 0
    answer = random.randint(1, 10)
    get_guess(attempts, answer, name)


def main():
    name = input("What is your name?  ")
    print(f"Welcome to the number guessing game {name}! 😄")
    start_game(name)
    while True:
        # Prompt player if they would like to replay
        replay_choice = (input("Would you like to play again? Y/N?  ")).lower()
        if replay_choice == "y":
            start_game(name)
        elif replay_choice == "n":
            sys.exit(
                f"Thank you for playing the random number guessing game {name} 😸")
        else:
            # Handle invalid input
            print('Oops 😕 ... please enter either "Y" or "N"')


if __name__ == "__main__":
    main()
