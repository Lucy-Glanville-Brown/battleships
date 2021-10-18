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

letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                      "F": 5, "G": 6, "H": 7}
# converts letters to numbers

numbers_to_letters = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E",
                      5: "F", 6: "G", 7: "H"}
# converts numbers to letters

user_score = 0
computer_score = 0


# Python program to print
# colored text and background
# Code taken from Geeks for Geeks, see README
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


def print_board(board):
    # Code taken from Knowledge Mavens video, see README
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
    # Code taken from Knowledge Mavens video, see README
    """
    Creates a random integer between 0 and 7 for ship_row and ship_column
    Checks if "@" is already on the board, if so runs randomint until
    there is an available space
    When there is an available space update with "@"
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "@":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "@"


def computer_guess(board):
    """
    Creates a random integer between 0 and 7 for computer_row and
    computer_column
    Checks if "-" or "X" is already on the board, if so runs randomint until
    there is an available space
    If computer_row and computer_column is "@", prints message to user to say
    their ship has been hit and updates board with "X"
    Else the computer_row and computer_column finds a blank space, prints
    message to the user to say the computer has missed and updates the
    board with "-"
    """
    global computer_score
    computer_row, computer_column = randint(0, 7), randint(0, 7)
    if (USER_BOARD[computer_row][computer_column] == "-" or
            USER_BOARD[computer_row][computer_column] == "X"):
        computer_row = randint(0, 7)
        computer_column = randint(0, 7)
    elif USER_BOARD[computer_row][computer_column] == "@":
        prCyan(f"{username}, your battleship has been hit!")
        prCyan(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        USER_BOARD[computer_row][computer_column] = "X"
        computer_score += 1
    else:
        prCyan(f"Phew {username}, the computer missed!")
        prCyan(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        USER_BOARD[computer_row][computer_column] = "-"


def get_ship_location():
    # Code taken from Knowledge Mavens video, see README
    """
    Asks user to input the guesses for ship row and ship column locations
    Checks input data for row is in range "12345678"
    Checks input data for column is in range "ABCDEFGH"
    Returns int for row - 1 to match index number, converts letters to numbers
    for column index number
    """
    row = input("Please enter a ship row 1-8\n")
    while row not in "12345678":
        validate_row(row)
        print("Please enter a valid row")
        row = input("Please enter a ship row 1-8\n")
    column = input("Please enter a ship column A-H\n").upper()
    while column not in "ABCDEFGH":
        validate_column(column)
        print("Please enter a valid column")
        column = input("Please enter a ship column A-H\n").upper()
    return int(row) - 1, letters_to_numbers[column]


def validate_row(values):
    """
    If values entered not an interger between 1-8 error message printed
    """
    try:
        [int(value) for value in values]
        if int(values) < 1 or int(values) > 8:
            raise ValueError(
                f"Number between 1-8 required, you provided {values}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def validate_column(values):
    """
    If values entered not in letters_to_numbers error message printed
    """
    try:
        if values not in letters_to_numbers:
            raise ValueError(
                f"Letter between A-H required, you provided {values}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def count_hit_ships(board):
    # Code taken from Knowledge Mavens video, see README
    """
    Counts how many ships on the board have been hit "X"
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def main():
    """
    Run all start up functions
    """
    create_ships(HIDDEN_BOARD)
    # print hidden board for testing, needs removing before submission
    # print("Hidden Board")
    # print_board(HIDDEN_BOARD)
    create_ships(USER_BOARD)
    prGreen("""\
______       _   _   _           _     _
| ___ \     | | | | | |         | |   (_)
| |_/ / __ _| |_| |_| | ___  ___| |__  _ _ __  ___
| ___ \/ _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|
| |_/ / (_| | |_| |_| |  __/\__ \ | | | | |_) \__ \.
\____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/
                                        | |
                                        |_|
        """)
    prCyan("""\
                                  )___(
                           _______/__/_
                  ___     /===========|   ___
 ____       __   [\\\]___/____________|__[///]   __
 \   \_____[\\]__/___________________________\__[//]___
  \40A                                                 |
   \                                                  /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)
    print("Welcome to Battleships")
    print("You have 10 turns to find all of the battleships")
    global username
    username = input("Please enter your name:\n")


def run_game():
    """
    Runs the game with 10 turns
    When turns = 0 game is over
    """
    # Code taken from Knowledge Mavens video, see README
    """
    I have added the user and computer scores, the if statement
    for if the computer wins, and the continue playing option
    """
    turns = 10
    global user_score

    while turns > 0:
        prGreen(f"{username}'s Board")
        print_board(USER_BOARD)
        prCyan("Computer's Board")
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-" or GUESS_BOARD[row][column] == "X":
            prRed("You have already guessed that")
        elif HIDDEN_BOARD[row][column] == "@":
            prGreen(f"Congratulations {username}, you have hit the battleship")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
            computer_guess(USER_BOARD)
            user_score += 1
        else:
            prGreen(f"Sorry {username}, you missed")
            GUESS_BOARD[row][column] = "-"
            turns -= 1
            computer_guess(USER_BOARD)
        if count_hit_ships(GUESS_BOARD) == 5:
            prGreen(
                f"Congratulations {username}, "
                "you have sunk all of the battleships")
            print("The game is now over")
            break
        prPurple("You have " + str(turns) + " turns remaining")
        prYellow(f"{username}'s Score: {user_score}"
                 f" Computer's Score: {computer_score}")
        if turns == 0:
            prGreen(
                f"Sorry {username}, you ran out of turns, the game is over")
            break
        if count_hit_ships(USER_BOARD) == 5:
            prGreen(
                f"Sorry {username}, the computer"
                " has sunk all of your battleships")
            break
        if count_hit_ships(GUESS_BOARD) < 5:
            continue_playing = input("Do you want to continue playing? y/n\n")
            if continue_playing == "y" or continue_playing == "yes":
                print(
                    "You have decided to continue playing the game.")
                continue
            elif continue_playing == "n" or continue_playing == "no":
                print(
                    "You have decided to finish playing, the game is now over")
                break
            else:
                print("Sorry, please can you enter y/n")
                continue_playing = input(
                    "Do you want to continue playing? y/n \n")


main()
run_game()
