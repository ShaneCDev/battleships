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


GRID_ALPHABET = 'ABCDEFGH'

# Boards 4x4
PLAYER_4x4 = [[" "]*4 for i in range(4)]
PLAYER_GUESSBOARD_4x4 = [[" "]*4 for i in range(4)]
COMPUTER_4x4 = [[" "]*4 for i in range(4)]
COMP_GUESSBOARD_4x4 = [[" "]*4 for i in range(4)]

# Boards 5x5
PLAYER_5x5 = [[" "]*5 for i in range(5)]
PLAYER_GUESSBOARD_5x5 = [[" "]*5 for i in range(5)]
COMPUTER_5x5 = [[" "]*5 for i in range(5)]
COMP_GUESSBOARD_5x5 = [[" "]*5 for i in range(5)]

# Boards 8x8
PLAYER_8x8 = [[" "]*8 for i in range(8)]
PLAYER_GUESSBOARD_8x8 = [[" "]*8 for i in range(8)]
COMPUTER_8x8 = [[" "]*8 for i in range(8)]
COMP_GUESSBOARD_8x8 = [[" "]*8 for i in range(8)]


LEN_OF_SHIPS = [5, 4, 3, 3, 2]


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
        board = PLAYER_4x4
        for row in board:
            print(f'{row_num} {"|".join(row)}')
            row_num += 1

    if grid_size == "M":
        print("  A B C D E")
        print("  +-+-+-+-+")
        board = PLAYER_5x5
        for row in board:
            print(f'{row_num} {"|".join(row)}')
            row_num += 1

    if grid_size == "L":
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        board = PLAYER_8x8
        for row in board:
            print(f'{row_num} {"|".join(row)}')
            row_num += 1

    return board


def place_ships(board):
    """
    Lets user place ships and does it randomly for computer
    """
    for ship_len in LEN_OF_SHIPS:
        if board == PLAYER_8x8:
            place_ship = True
            print("Place the " + str(ship_len) + " length ship")


def check_out_of_bounds_8x8(ship_len, row, col, orientation, board):
    """
    Check and see if the ship is in a legal placement on the 
    8x8 board
    """
    if orientation == "V" and board == PLAYER_8x8:
        if row + ship_len > 8:
            return False
        else:
            return True
    elif orientation == "H" and board == PLAYER_8x8:
        if col + ship_len > 8:
            return False
        else:
            return True


def check_out_of_bounds_5x5(ship_len, row, col, orientation, board):
    """
    Check and see if the ship is in a legal placement on the
    5x5 board
    """
    if orientation == "V" and board == PLAYER_5x5:
        if row + ship_len > 5:
            return False
        else:
            return True
    elif orientation == "H" and board == PLAYER_5x5:
        if col + ship_len > 5:
            return False
        else:
            return True


def check_out_of_bounds_4x4(ship_len, row, col, orientation, board):
    """
    Check and see if the ship is in a legal placement on the
    4x4 board
    """
    if orientation == "V" and board == PLAYER_4x4:
        if row + ship_len > 4:
            return False
        else:
            return True
    elif orientation == "H" and board == PLAYER_4x4:
        if col + ship_len > 4:
            return False
        else:
            return True


def user_input(place_ship):
    """
    Function to be used within the place ships
    function, doing it this way is a lot easier
    for placing ships and cleaner.
    """
    if place_ship:
        while True:
            try:
                orientation = input("Would you like to place the ship " +
                                    "horizontal" +
                                    "or vertical? (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print("Enter 'H' or 'V' only.")


def hit_counter(board):
    """
    Hit counter for when a ship is hit by either
    user or computer
    """
    hits = 0
    for row in board:
        for col in board:
            if col == "■":
                hits += 1

    return hits

