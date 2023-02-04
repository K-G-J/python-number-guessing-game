"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import sys

name = input("What is your name?  ")

print(f"Welcome to the number guessing game {name}! 😄")


def get_guess(attempts, answer):
    try:
        guess = int(
            input("Try to guess the random number between 1 and 10.  "))
        if guess > 10 or guess < 1:
            # Handle out of range guesses
            print(
                f"{guess} is out of range 😕 the random number is between 1 and 10")
            attempts += 1
        elif guess > answer:
            print("It's lower ⬇")
            attempts += 1
            get_guess(attempts, answer)
        elif guess < answer:
            print("It's higher ⬆")
            attempts += 1
            get_guess(attempts, answer)
        else:
            # Correct guess
            print(
                f"Got it! 🥳 \n It took {attempts} attempts to get the correct number \n Game over 👋. \n Thank you for playing {name} 😄")
    except ValueError as err:
        # Handle invalid value guesses
        print("Oh no! That's not a valid number 😕. Try again...")
        print(f"({err})")
        attempts += 1
        get_guess(attempts, answer)
    else:
        return guess


def replay_prompt():
    replay_choice = (input("Would you like to play again? Y/N?  ")).lower()
    if replay_choice != "y" and replay_choice != "n":
        print('Oops 😕 ... please enter either "Y" or "N"')
        replay_prompt()
    return replay_choice


def start_game():
    # Reset attempts and new random number before each round
    attempts = 0
    answer = random.randint(1, 10)
    get_guess(attempts, answer)
    # Prompt player if they would like to replay
    replay_choice = replay_prompt()
    if replay_choice == "n":
        sys.exit(
            f"Thank you for playing the random number guessing game {name} 😸")
    while replay_choice == "y":
        start_game()


start_game()


"""
Extra Credit

4 steps
    2.  As a player of the game, after I guess correctly I should be prompted if I would like to play again.
    3.  As a player of the game, at the start of each game I should be shown the current high score (least amount of points) so that I know what I am supposed to beat.
    4.  Every time a player decides to play again, the random number to guess is updated so players are guessing something new each time.
"""
