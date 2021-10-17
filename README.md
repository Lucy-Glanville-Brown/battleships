# Battleships Game
## Portfolio Project 3 - Code Institute
Battleships is a game which I think most people would have played at some point in their lives. This Battleships game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.
The users have 10 turns to find all of the computer’s battleships before the computer finds theirs. Each battleship occupies one space on the board.

![Am i responsive](https://user-images.githubusercontent.com/85178695/137642707-6797f684-de8c-4ff0-9e3a-a6bb3ec29c3b.png)


View the live project [here](https://battleships01.herokuapp.com/)

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
* User and computer scores calculated and printed to terminal
* Turns remaining calculated and printed to the terminal
* Continue playing option for the user to input y/n
* Users board updated with hit or miss and re-printed
* Computers board updated with hit or miss and re-printed
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

When the game is loaded the game name, welcome message, game instructions and user's name input field are displayed correctly.
* Display game name
* Display game info
* User inputs name

![loading screen](https://user-images.githubusercontent.com/85178695/137600517-3cb4a091-9244-4288-bf94-72c3800a2bef.png)

When the user inputs their name two boards are created, one for the user and their ships and another board for the computer which is blank for the user to guess the computers ships.
* User board displayed with ship locations for the computer to guess
* Computer board displayed for the user to guess the computers ship locations

![game boards](https://user-images.githubusercontent.com/85178695/137600529-586d627d-6075-4b34-9905-8a19f32defe6.png)

When the user inputs a row number this is validated to see if it is a number between 1-8. I have tested the validation by using a number outside of the range, a letter and a word and the data validation error message displays until the correct input type has been entered.
* User inputs guess for row
* User input validated for correct input

![row validation](https://user-images.githubusercontent.com/85178695/137600543-b87292f3-a6a6-4a6c-bc7f-87c6146090f9.png)


When the user inputs a column letter this is validated to see if it is a letter between A-H. I have tested the validation by using a letter outside of the range, a word, and a number and the data validation error message displays until the correct input type has been entered.
* User inputs guess for column
* User input validated for correct input

![column validation](https://user-images.githubusercontent.com/85178695/137600547-91f476d5-3c10-471e-87b2-7b8e994666ce.png)


Once the user has input the row and column coordinates, these are checked against the HIDDEN_BOARD to see if the user has hit or missed. A message is printed to the user with the hit or miss result. The computers guess is randomly generated and checked against the users board and a message to the user is displayed with the hit or miss result. A message with the computers guess coordinates are printed to the user. The turns remaining is display as well as the user's and computer's scores. Message is displayed to the user asking if they want to continue playing.
* User’s input coordinates are checked against the hidden board
* Message to user to display if their guess was a hit or a miss
* Computers guesses are randomly generated
* Computers guesses are checked against the user board
* Message to user to display if the computer guess was a hit or miss
* User and computer scores calculated and printed to terminal
* Turns remaining calculated and printed to the terminal
* Continue playing option for the user to input y/n

![end of round](https://user-images.githubusercontent.com/85178695/137600572-43b7c608-5873-44ec-9982-7387655dba42.png)


If the user inputs n a message is displayed and the game ends

![continue playing n](https://user-images.githubusercontent.com/85178695/137600586-248f40a6-0a6b-443f-a422-4801fbed9e5e.png)

If the users inputs y a message is display and the game continues

![continue playing y](https://user-images.githubusercontent.com/85178695/137600591-14a7bbde-da73-44bc-9131-24bab936e16f.png)


When the user hits a ship the correct message is displayed and their score is incremented by 1.

![computer ship been hit](https://user-images.githubusercontent.com/85178695/137600653-3d1313a8-949e-4bb9-bb05-a920c405de09.png)


When the computer hits a ship the correct message is displayed and their score is incremented by 1.

![user ship been hit](https://user-images.githubusercontent.com/85178695/137600661-2d48ca27-713f-48a7-9668-16053c994ee7.png)


The users board and computer board are updated with the guesses and reprinted. The game continues until the user either quits, hits all 5 ships, the computer hits all 5 ships of the user has run out of turns.
* Users board updated with hit or miss and re-printed
* Computers board updated with hit or miss and re-printed

![boards updated and reprinted](https://user-images.githubusercontent.com/85178695/137600701-634f9fee-f933-42a0-9022-9bcdad9c72f6.png)


When the user hits all 5 ships a message is display and the game finishes.
* If user has hit 5 ships display message for winning game and end game

![user hit 5 ships](https://user-images.githubusercontent.com/85178695/137600704-afdeb5a8-fb5a-44df-8dc9-dfa84c66357e.png)


In the github terminal I changed turns from 10 to 80 in the run_game function to test if the computer could win the game when not restricted to 10 turns. I was unable to test this successfully as there is a bug which has been documented in the bugs section.
* If computer has hit 5 ships display message for losing game and end game


* If user has run out of turns display message and end game

![run out of turns](https://user-images.githubusercontent.com/85178695/137600717-cc0bd793-8a21-4dc2-87e7-34c8b035a52b.png)


### Bugs
The computer guesses were not being updated on the user's board but I had noticed that I was not calling the correct variable names. This has now been corrected and the boards are being updated as expected.

![bug run out turns](https://user-images.githubusercontent.com/85178695/137642822-cbe2007e-4154-470f-8e53-52c62dd93559.png)


When testing the game I have noticed that sometimes the computer guess is not generated and the messages are not printed to the screen. I have tested this several times and I have not been able to find any logic in why this is happening as it seems to be at random times.  

![copmputer guess not generated](https://user-images.githubusercontent.com/85178695/137642829-9ce6ed20-8a12-4e4d-b3eb-90f12b1c5fff.png)


### Validator Testing
PEP8

![PEP8 Validator](https://user-images.githubusercontent.com/85178695/137600734-85b09ca6-42d9-41c9-b2a6-5976a06d6b98.png)


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
* Knowledge Mavens for the YouTube video How to Code Battleship in Python - Single Player Game. [Knowledge Mavens Video](https://www.youtube.com/watch?v=tF1WRCrd_HQ)
* The battleships text in ascii was created using an ascii generator found [here](https://patorjk.com/software/taag/#p=display&f=Doom&t=Battleships)
* The battleship image in ascii was taken from [here](https://www.asciiart.eu/vehicles/navy)
* After running the code through the PEP8 validator I had a lot of errors for the lines being too long which I found help on stack overflow [here](https://stackoverflow.com/questions/3346230/wrap-long-lines-in-python/18160132)
* PEP8 validator error local-variable-referenced-before-assignment I also found help on stack overflow [here](https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment)
* Another error I had after using PEP8 was that my if statement line was too long, I found help on stackoverflow and flake8rules
[stackoverflow](https://stackoverflow.com/questions/5253348/very-long-if-statement-in-python)
[flake8rules](https://www.flake8rules.com/rules/E129.html)


## Acknowledgements
The basic layout of the code was written by following along with the Knowledge Mavens YouTube video on How to Code Battleship in Python - Single Player. I used Repl to code along with the video and the original code can be found [here.](https://replit.com/@lucygbrown/battleships#main.py)

I watched this video several times and made notes as I was going along to break down each step. This video was just for single player so I have created another board which shows the users board with ships for the computer to guess. I have also added data validation for the input of the row and column coordinates as well as a contiune playing option. 

The code that I have added is:
* USER_BOARD
* numbers_to_letters
* user_score
* computer_score
* computer_guess(board)
* validate_row(values)
* validate_column(values)
* main()
    * Battleships ascii text
    * Battleship ascii art
    * username input
* run_game()
    * Updated the printed messages to f strings to include the user's name
    * Print the USERS_BOARD
    * Added computer_guess(USERS_BOARD) to the if statments for if the ship location was a hit or miss
    * Added continue playing option and if statments



My mentor Nishant Kumar suggested adding colour to the game which was found on Geeks for Geeks website [here.](https://www.geeksforgeeks.org/print-colors-python-terminal/)







