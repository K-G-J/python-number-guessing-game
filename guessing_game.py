"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

# Game parameters
MIN = 1
MAX = 10
GUESS_PROMPT = f"Try to guess the random number between {MIN} and {MAX}.  "

# Greet the player by name
NAME = input("What is your name?  ")
print(f"Welcome to the number guessing game {NAME}! 😄")


def play_game(answer):
    attempts = 0
    while True:
        attempts += 1
        try:
            while (guess := int(input(GUESS_PROMPT))) not in range(MIN, MAX + 1):
                # Handle out of range guesses
                print(
                    f"{guess} is out of range 😕 the random number is between {MIN} and {MAX}")
        except ValueError as err:
            # Handle invalid input guesses
            print(
                f"Oh no! That's not a valid number 😕. Try again... \n ({err})")
            continue
        if guess == answer:
            # Handle correct guess
            print(
                f"Got it! 🥳 \n It took {attempts} attempt{'' if attempts == 1 else 's'} to get the correct number \n Game over 👋. \n Thank you for playing {NAME} 😄")
            return attempts
        elif guess > answer:
            print("It's lower ⬇")
        elif guess < answer:
            print("It's higher ⬆")
        else:
            print("Oops 😕 ... something went wrong. Please try again.")

def main():
    high_score = 0

    attempts = play_game(random.randint(1, 10))

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
            attempts = play_game(random.randint(1, 10))
        elif replay_choice == "n":
            print(
                f"Thank you for playing the random number guessing game {NAME} 😸")
            return
        else:
            # Handle invalid input
            print('Oops 😕 ... please enter either "Y" or "N"')


if __name__ == "__main__":
    main()
