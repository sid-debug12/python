""" a simple geusing number game where the user tries to guess a random number."""

import random
import sys
import emoji
from enum import Enum


def gn(name: str):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_gn():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        class GN(Enum):
            first = 1
            second = 2
            third = 3

        print(emoji.emojize("Welcome to Guess the number! :game_die:"))
        player_choice = input(
            f" {name}, please enter a number between 1 and 3: ")
        if player_choice not in ['1', '2', '3']:
            print(f"{name}, please enter a number between 1 and 3.")
            return play_gn()

        player = int(player_choice)
        computer_choice = random.choice([1, 2, 3])
        computer = int(computer_choice)

        print(" ")

        print(f"{name} chose {str(GN(player)).replace('GN.', '')}")
        print(f"Computer chose {str(GN(computer)).replace('GN.', '')}")

        print(" ")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins

            if player == computer:
                player_wins += 1
                return f"{name}, you guessed right!"

            else:
                computer_wins += 1
                return f"Sorry {name}, you got wrong guess."

        result = decide_winner(player, computer)
        print(result)

        nonlocal game_count
        game_count += 1
        print(f"{name} score: {player_wins}, computer score: {computer_wins}")

        play_again = input("DO you want to play again? (y/n):")

        while True:
            play_again = input("\n Play again? (y/n): ")
            if play_again.lower() not in ["y", "n"]:
                print(
                    f"{name}, you entered an invalid input. Please enter 'y' or 'n'.")
                continue
            else:
                break
        if play_again.lower() == "y":
            return play_gn()
        else:
            play_again = False
            print("\nThank you for playing!")
            sys.exit(f"Bye {name}!")
    return play_gn
