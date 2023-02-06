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
REPLAY_PROMPT = "Would you like to play again? Y/N?  "

# Greet the player by name
NAME = input("What is your name?  ")
print(f"Welcome to the number guessing game {NAME}! 😄")


def play_game(answer):
    attempts = 0
    while True:
        # Increase guess attempts each iteration
        attempts += 1
        try:
            guess = int(input(GUESS_PROMPT))
        except ValueError as err:
            # Handle invalid input guesses
            print(
                f"Oh no! That's not a valid number 😕. Try again... \n ({err})")
            continue
        if guess not in range(MIN, MAX + 1):
            # Handle out of range guesses
            print(
                f"{guess} is out of range 😕 the random number is between {MIN} and {MAX}")
            continue

        if guess == answer:
            # Handle correct guess and tell player number of attempts
            print(
                f"Got it! 🥳 \n It took {attempts} attempt{'' if attempts == 1 else 's'} to get the correct number \n Game over 👋. \n Thank you for playing {NAME} 😄")
            return attempts

        # Tell player if guess is higher or lower than answer
        print("It's lower ⬇") if guess > answer else print("It's higher ⬆")


def main():
    
    # Declare initial high score variable
    high_score = 0

    while True:
        # Set new random number before each round
        attempts = play_game(random.randint(MIN, MAX))

        # Set and display high score
        if high_score == 0 or attempts < high_score:
            high_score = attempts
            print("You set the high score! 🤩")

        print(f"The current high score is {high_score} 🤗")

        # Prompt player if they would like to replay
        while (replay_choice := (input(REPLAY_PROMPT)).lower()) != "n":
            if replay_choice == "y":
                # Break out of replay prompt and start new round
                break
            else:
                # Handle invalid input
                print('Oops 😕 ... please enter either "Y" or "N"')
        else:
            # Display ending message
            print(
                f"Thank you for playing the random number guessing game, {NAME} 😸")
            return


if __name__ == "__main__":
    main()
