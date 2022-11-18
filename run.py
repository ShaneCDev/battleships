import random
import os
import sys

letters_to_numbers = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7
}
GUESS_BOARD = [[" "]*8 for i in range(8)]


def welcome_message():
    """
    Welcome message for the user explaining the rules
    of the game
    """
    print("Welcome to battleships!")
    print("Just some stuff to go over before we begin.")
    print("Ships must be placed vertically or horizontally - not diagonally.")
    print("Ships can not hang off the grid.")
    print("Ships can touch each other but not occupy the same grid space.")
    print("You can not change ships postions once the game has begun.")
    print("Both players take turns firing shots by using grid coordinates.")
    print("The first person to sink all of your opponents ships wins!")
    print("With that being said, good luck!")


def print_board(board):
    """
    Prints game board
    """
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_num = 1
    for row in board:
        print(f'{row_num} {"|".join(row)}')
        row_num += 1
    return board




