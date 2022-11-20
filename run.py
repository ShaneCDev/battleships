from random import randint
import os
import sys

# grid sizes = 4x4, 5x5, 7x7
# X - ship hit
# '-' - ship miss
# ■ - ship(s)


SHIP = '■'
NAME = ''

letters_to_numbers = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7
}

GUESS_BOARD_LARGE = [[" "]*8 for i in range(8)]
COMPUTER_BOARD_LARGE = [[" "]*8 for i in range(8)]
GRID_ALPHABET = 'ABCDEFGH'


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


def create_ships(comp_board):
    """
    Creates ships for the computer.
    """

    for i in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while comp_board[ship_row][ship_column] == "~":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        comp_board[ship_row][ship_column] = "~"


def user_select_grid_size():
    """
    Lets user select the size of the grid
    """
    print("How big or small would you like the grid to be?")
    print("Small: 4x4, Medium: 5x5, Large: 8x8?")
    print("Choose the size by typing S/M/L")
    grid_size = input().upper()
    board = ''
    row_num = 1

    if grid_size == "S":
        print("  A B C D")
        print("  +-+-+-+")
        board = [[" "]*4 for i in range(4)]
        for row in board:
            print(f'{row_num} {"|".join(row)}')
            row_num += 1

    if grid_size == "M":
        print("  A B C D E")
        print("  +-+-+-+-+")
        board = [[" "]*5 for i in range(5)]
        for row in board:
            print(f'{row_num} {"|".join(row)}')
            row_num += 1

    if grid_size == "L":
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        board = [[" "]*8 for i in range(8)]
        for row in board:
            print(f'{row_num} {"|".join(row)}')
            row_num += 1

    return board


def place_ships():
    """
    Lets user place ships and does it randomly for computer
    """


user_select_grid_size()
