# Battleships Game
## Portfolio Project 3 - Code Institute
Battleships is a game which I think most people would have played at some point in their lives. This Battleships game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.
The users have 10 turns to find all of the computer’s battleships before the computer finds theirs. Each battleship occupies one space on the board.

### How to play
In this version the player enters their name and two boards are randomly generated. The first board displayed is the user’s board which shows the locations of the ships which the computer needs to find. The second board is the computer’s board which is where the user’s guesses will be updated, this will not show the ship locations until the user has hit one of the ships. If a guess misses the battleship “-“ will be display, when a battleship has been hit “X” will be displayed. The player and the computer then take turns to make guesses to try and sink each others battleships. The winner is the player who can sink all of the battlehips first before they run out of turns.

## User Stories
Create a Python terminal based game where the users challenges the computer.
* Display game name
* Display game info
* User inputs name
* User board displayed with ship locations for the computer to guess
* Computer board displayed for the user to guess the computers ship locations
* User inputs guess for row
* User input validated for correct input
* User inputs guess for column
* User input validated for correct input
* User’s input coordinates are checked against the hidden board
* Message to user to display if their guess was a hit or a miss
* Computers guesses are randomly generated
* Computers guesses are checked against the user board
* Message to user to display if the computer guess was a hit or miss
* Users board updated with hit or miss and re-printed
* Computers board updated with hit or miss and re-printed
* User and computer scores calculated and printed to terminal
* Turns remaining calculated and printed to the terminal
* If user has hit 5 ships display message for winning game and end game
* If computer has hit 5 ships display message for losing game and end game
* If user has run out of turns display message and end game

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


In this game of Battleships, the player and computer each have up to 10 turns to find the opponents 5 battleships, and the winner if whoever finds all 5 first.

There are three boards, the Player's Board and the Computer's Board which are both displayed, and a hidden board which holds the position of the computer's battleships which the player needs to find.

Each  board has 8 rows and 8 columns, the rows are 1 to 8, and the columns are A to H, and each cell contains a spaces.


Each battleship occupies one cell, and before the game starts, the computer generates the position of 5 battleships that the player and computer need to find to win, and populates the player and hidden boards with them by replacing the space with a "@". The computer board is left blank so that the player cannot see the computers choices.

The Player enters a ship row and column, and the computer generates a ship row and column. 

If the player row and column does not find a battleship on the computers hidden board, the message "Sorry you missed" is displayed and the cell of the displayed computer board is populated with a -.

If the player row and column does find a battleship on the computers hidden board, the message "congratulations you have hit the battleship" is displayed and the cell of the displayed computer board is populated with an X.

The computers generated row and column are displayed.

If the computer row and column does not find a battleship on the players board, the message "Phew the computer missed" is displayed and the cell of the players board is replaced with an -.

If the computer row and column does find a battleship on the players board, the message "your battleship has been hit" is displayed and the @ in the cell is replaced with an X.

After each turn, the number of turns remaining is displayed and control returns for the player to enter their next row and column if the turns are under 10.

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
The computer guesses were not being updated on the user's board but I had noticed that I was not calling the correct variable names. This has now been corrected and the boards are being updated as expected.

### Validator Testing
PEP8

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
* Fork or Clone this repository
* Create new Heroku app
* You will need to add PORT 8000 to Config Vars in the Settings tab
* Set the buildbacks to Python and NodeJS in that order
* In the Deployment tab select GitHub as the Deployment method
* Link the Heroku app to the repository
* Click on Deploy

## Credits
* Code Institute for the deployment terminal
* Knowledge Mavens for the YouTube video How to Code Battleship in Python - Single Player Game. https://www.youtube.com/watch?v=tF1WRCrd_HQ




