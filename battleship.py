"""
Welcome to Battleship!
In this project you will build a simplified, one-player version of the classic board game Battleship!
In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid.
The player will have 10 guesses to try to sink the ship.
"""
#Board
board = []

#Create a 5 x 5 grid initialized to all 'O's and store it in board.
board = []
for i in range(0, 5):
    board.append(["O"] * 5)
    
#Define print_board function    
def print_board(board):
    for item in board:
        print " " .join(item)

print_board(board)