import sys
from enum import Enum
from rps import rock_paper_scissos
from guess_game import guess_game


class Choose(Enum):
    first = 1
    second = 2

    print("Welcome to guessing master")
    player_choice = input(
        "\nChoose a game within the numbers ['1', '2']: ")
