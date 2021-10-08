from random import randint

# Legend
# "X" for placing ship and hit battleship
# " " for available space
# "-" for missed shot

HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# creates a list of 8 spaces, 8 times
GUESS_BOARD = [[" "] * 8 for x in range(8)]
# creates a list of 8 spaces, 8 times


def print_board(board):
    """
    Creates a board with letters for the columns and numbers for the rows with | separator

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
    Checks if "X" is already on the board, if so runs randomint until there is an available space
    When there is an available space update with "X"
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = "X"


create_ships(HIDDEN_BOARD)
print("print board hidden board")
print_board(HIDDEN_BOARD)
create_ships(GUESS_BOARD)
print("print board guess board")
print_board(GUESS_BOARD)

