from random import randint
import os
import sys

# grid sizes = 3x3, 4x4, 5x5, 7x7
# X - ship hit
# '-' - ship miss
# ~ - ship(s)

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


def create_ships(comp_board):
    """
    Creates ships for the computer.
    """
    print("Enter the coordinates you would like to place your ships.")
    print("Separate each coordinate with a comma, eg. A,4")

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
    print("Small: 3x3, Medium: 5x5, Large: 7x7?")
    print("Choose the size by typing S/M/L")
    grid_size = input().upper()
    
    row_num = 1

    if grid_size == "S":
        print(" A B C")
        print(" +-+-+")
        small_board = [[" "]*4 for i in range(4)]
        for row in small_board:
            print(f'{row_num} {"|".join(row)}')
            row_num += 1
        return small_board
    
            
user_select_grid_size()


