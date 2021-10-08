from random import randint

# Legend
# "X" for placing ship and hit battleship
# " " for available space
# "-" for missed shot

HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# creates a list of 8 spaces, 8 times
GUESS_BOARD = [[" "] * 8 for x in range(8)]
# creates a list of 8 spaces, 8 times

letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
# converts letters to numbers

def print_board(board):
    """
    Creates a board with letters for the columns and numbers for the rows
    """
    print("  A B C D E F G H")
    print("  ---------------")
    row_number = 1
    for row in board:
        print(row_number, "|".join(row))
        row_number += 1

def create_ships(board):
    """
    Creates a random integer between 0 and 7 for ship_row and ship_column
    Checks if "X" is already on the board, if so runs randomint until
    there is an available space
    When there is an available space update with "X"
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = "X"

def get_ship_location():
    """
    Asks user to input the guesses for ship row and ship column locations
    Checks input data for row is in range "12345678"
    Checks input data for column is in range "ABCDEFGH"
    Returns int for row - 1 to match index number, converts letters to numbers
    for column index number
    """
    row = input("Please enter a ship row 1-8\n")

    while row not in "12345678":
        print("Please enter a valid row")
        row = input("Please enter a ship row 1-8\n")
    
    column = input("Please enter a ship column A-H\n").upper()

    while column not in "ABCDEFGH":
        print("Please enter a valid column")
        column = input("Please enter a ship column A-H\n").upper()
    return int(row) - 1, letters_to_numbers[column]

def count_hit_ships(board):
    """
    Counts how many ships you have hit
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count



create_ships(HIDDEN_BOARD)
print("print board hidden board")
print_board(HIDDEN_BOARD)
create_ships(GUESS_BOARD)
print("print board guess board")
print_board(GUESS_BOARD)
get_ship_location()

