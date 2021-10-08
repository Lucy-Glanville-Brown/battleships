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

print("print board hidden board")
print_board(HIDDEN_BOARD)
print("print board guess board")
print_board(GUESS_BOARD)