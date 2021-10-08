from random import randint

# Legend
# "X" for placing ship and hit battleship
# " " for available space
# "-" for missed shot

HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
GUESS_BOARD = [[" "] * 8 for x in range(8)]

print("hidden board")
print(HIDDEN_BOARD)
print("guess board")
print(GUESS_BOARD)
