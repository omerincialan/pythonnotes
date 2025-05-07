"""
CS3B, Assignment #03, Tic Tac Toe Part 2
Omer Incialan
In this assignment, I replaced the ArrayGameBoard class I created in the first 
part of this assignment with BitGameBoard in which I implemented the same 
methods and same functionalities with ArrayGameBoard. 
In the BitGameBoard, I built the same functionality of existing methods in 
ArrayGameBoard by benefiting from bit operations by using a single int.

Additionally, I created a HumanPlayer class which I used as an alternating player 
side for X and O.

Finally, I created a ttt_game function in which I let users to play the game
 and declare winner.
"""

from enum import Enum

# GameBoardPlayer Enum
class GameBoardPlayer(Enum):
    NONE = 0
    X = 1
    O = 2
    DRAW = 3
    
    def __str__(self):
        return " " if self == GameBoardPlayer.NONE else self.name

# BitGameBoard Class
class BitGameBoard:
    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.board = 0  # Use an integer to represent the board

    def get_nrows(self):
        return self.nrows

    def get_ncols(self):
        return self.ncols

    def set(self, row, col, value):
        position = (row * self.ncols + col) * 2
        mask = 3 << position
        self.board &= ~mask  # Clear the bits at the position
        self.board |= value.value << position  # Set new value

    def get(self, row, col):
        position = (row * self.ncols + col) * 2
        return GameBoardPlayer((self.board >> position) & 3)

    def __str__(self):
        board_str = ''
        for row in range(self.nrows):
            # Construct each row
            row_str = ' | '.join(str(GameBoardPlayer(self.get(row, col))) for col in range(self.ncols))
            board_str += row_str
    
            # Add row separator, except after the last row
            if row < self.nrows - 1:
                board_str += '\n' + '--+-' * (self.ncols - 1) + '--\n'
        return board_str

    def get_winner(self):
        # Check rows and columns for a winner
        for i in range(self.nrows):
            if all(self.get(i, j) == self.get(i, 0) != GameBoardPlayer.NONE for j in range(self.ncols)):
                return self.get(i, 0)
        for j in range(self.ncols):
            if all(self.get(i, j) == self.get(0, j) != GameBoardPlayer.NONE for i in range(self.nrows)):
                return self.get(0, j)
    
        # Check diagonals for a winner (only for square boards)
        if self.nrows == self.ncols:
            # Main diagonal
            if all(self.get(i, i) == self.get(0, 0) != GameBoardPlayer.NONE for i in range(self.nrows)):
                return self.get(0, 0)
            # Anti-diagonal
            if all(self.get(i, self.ncols - 1 - i) == self.get(0, self.ncols - 1) != GameBoardPlayer.NONE for i in range(self.nrows)):
                return self.get(0, self.ncols - 1)
    
        # Check for a draw
        if all(self.get(i, j) != GameBoardPlayer.NONE for i in range(self.nrows) for j in range(self.ncols)):
            return GameBoardPlayer.DRAW
    
        # No winner yet
        return GameBoardPlayer.NONE


# HumanPlayer Class
class HumanPlayer:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"Human player {self.side.name}"

    def get_move(self, board):
        while True:
            try:

                move = input(f"Player {self.side}, enter your move (row col): ")
                row, col = map(int, move.split())
                print(f">>> Human player {self.side} makes moves {row} - {col} ")
                if board.get(row, col) == GameBoardPlayer.NONE:
                    return row, col
                else:
                    print("This cell is already taken. Try again.")
                
            except (ValueError, IndexError):
                print("Invalid move. Please enter row and column as two integers separated by a space.")

# TicTacToe Game Function
def ttt_game(player1, player2):
    board = BitGameBoard(4, 4)  # 3x3 Tic-Tac-Toe board
    current_player = player1

    while True:
        print(board)  # Print the current state of the board
        row, col = current_player.get_move(board)

        # Check if the cell is already taken
        if board.get(row, col) != GameBoardPlayer.NONE:
            print(f"Cell {row}, {col} is already occupied. Please choose another.")
        
        #current_player = player2 if current_player == player1 else player1
       
        
        board.set(row, col, current_player.side)  # Make the move

        current_player = player2 if current_player == player1 else player1
        winner = board.get_winner()
        if winner != GameBoardPlayer.NONE:
            print(board)  # Print the final state of the board
            if winner == GameBoardPlayer.DRAW:
                print("\n ---> The game is a DRAW.")
                break
            else:
                print(f"\n ---> {winner} wins! $$$$")
                break  # Exit the loop if there's a winner or a draw
        continue  # Skip the rest of the loop and ask for input again
        # Switch sides after a valid move


if __name__ == '__main__':
    player1 = HumanPlayer(GameBoardPlayer.X)
    player2 = HumanPlayer(GameBoardPlayer.O)
    ttt_game(player1, player2)
