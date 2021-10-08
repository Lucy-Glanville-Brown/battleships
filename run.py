from random import randint

# Legend
# "@" for placing ship
# " " for available space
# "X" for hit battleship
# "-" for missed shot

HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# creates a list of 8 spaces, 8 times
GUESS_BOARD = [[" "] * 8 for x in range(8)]
# creates a list of 8 spaces, 8 times
USER_BOARD = [[" "] * 8 for x in range(8)]
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
    When there is an available space update with "@"
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "@":
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = "@"

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

def run_game():
  create_ships(HIDDEN_BOARD)
  print("Hidden Board")
  print_board(HIDDEN_BOARD)
  create_ships(USER_BOARD)
  print("Welcome to Battleships")
  print("You have 10 turns to find all of the battleships")
  global username
  username = input("Please enter your name:\n")

run_game()

turns = 10

while turns > 0:
    print(f"{username}'s Board")
    print_board(USER_BOARD)
    print("Computer's Board")
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == "-" or GUESS_BOARD[row][column] == "X":
        print("You have already guessed that")
    elif HIDDEN_BOARD[row][column] == "@":
        print("Congratulations, you have hit the battleship")
        GUESS_BOARD[row][column] = "X"
        turns -= 1
    else:
        print("Sorry, you missed")
        GUESS_BOARD[row][column] = "-"
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print("Congratulations, you have sunk all of the battleships")
        print("The game is now over")
        break
    print("You have " + str(turns) + " turns remaining")
    if turns == 0:
        print("Sorry, you ran out of turns, the game is over")
        break
