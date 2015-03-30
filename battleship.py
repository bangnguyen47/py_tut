"""
Welcome to Battleship!
In this project you will build a simplified, one-player version of the classic board game Battleship!
In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid.
The player will have 10 guesses to try to sink the ship.
"""

from random import randint

#Board
board = []

#Create a 5 x 5 grid initialized to all 'O's and store it in board.
for i in range(0, 5):
    board.append(["O"] * 5)
    
#Define print_board function    
def print_board(board):
    for row in board:
        print " " .join(row)

print "Let's play Battleship!"
print_board(board)

# Random row
def random_row(board):
    row = randint(0, len(board) - 1)
    return row
    
# Random column
def random_col(board):
    col = randint(0, len(board) - 1)
    return col

ship_row = random_row(board)
ship_col = random_col(board)

# Input row, col
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

print ship_row
print ship_col

if(guess_row == ship_row and guess_col == ship_col):
    print "Congratulations! You sank my battleship!"
else:
    
    if (guess_row not in range(5) or guess_col not in range(5)):
        print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
	
	print_board(board)