def create_board():
    """
    Creates the game board
    """
    height = int(input("How high would you like the grid to be?\n"))
    width = int(input("How wide would you like the grid to be?\n"))
    
    grid = [[row, col] for row in range(height) for col in range(width)]

    print(grid)


create_board()
