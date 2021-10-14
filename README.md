# Battleships Game
## Portfolio Project 3 - Code Institute
Battleships is a game which I think most people would have played at some point in their lives. This Battleships game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.
The users have 10 turns to find all of the computer’s battleships before the computer finds theirs. Each battleship occupies one space on the board.

### How to play
In this version the player enters their name and two boards are randomly generated. The first board displayed is the user’s board which shows the locations of the ships which the computer needs to find. The second board is the computer’s board which is where the user’s guesses will be updated, this will not show the ship locations until the user has hit one of the ships. If a guess misses the battleship “-“ will be display, when a battleship has been hit “X” will be displayed. The player and the computer then take turns to make guesses to try and sink each others battleships. The winner is the player who can sink all of the battlehips first before they run out of turns.

## Features
### Existing Features
* Random board generation for user board which places ships on the board
* Random board generation for hidden board which places ships on a board which the user cannot see
* Play against the computer
* Accepts user input for Name, Row and Column
* Maintains scores
* Input validation and error-checking
    * The user cannot enter coordinates outside of the grid
    * The user cannot enter the same coordinates twice
    * The user must enter a number between 1-8 for rows
    * The user must enter a letter between A-H for columns
* Randomly creates the computer guesses

### Future Features
* Allow the user to select the board size
* Allow the user to select the number of ships
* Allow the user to position the ships themselves
* Have ships larger than 1x1
* Different game modes
    * Not limited to 10 turns
    * Option to select how many turns you would like

## Testing
I have manually tested this project by doing the following:
* Run the code through the PEP8 validator and confirmed there are no problems
* Tested in the terminal on Gitpod and the Code Institute Heroku Terminal

### Bugs

### Validator Testing
PEP8


