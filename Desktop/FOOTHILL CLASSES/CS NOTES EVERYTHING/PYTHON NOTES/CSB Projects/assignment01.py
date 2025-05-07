"""
CS3B, Assignment #1, Tic Tac Toe (Part 1)
Omer Incialan
In this program, I improved the starter code by writing two classes and 
their methods.
First class is GameBoardPlayer, a simple enum class that represents 
either the player on a certain space or the winner at a certain step
Second class is the board on which the game takes place. 
Inside this class, with the help of methods, 
1- I defined number of rows, columns
rules and limitations on the rowXcolumn matrix. 
2- A dunder method returning the current situation of the board at a 
certain moment
3- A setter method which assigns a value (X, O, " ")  to a space on the 
board. A getter method as well.
4- A get_winner method which evaluates and returns the winner on the 
board based on general tictactoe rules.
"""

import time
from enum import Enum


class GameBoardPlayer(Enum):
    """ class that acts as a player """
    NONE = 0
    X  = 1
    O = 2
    DRAW = 3
    
    def __str__(self):
        return " " if self == GameBoardPlayer.NONE else self.name



class ArrayGameBoard:
    """ class that represents a rectangular game board"""

    def __init__(self, nrows, ncols):
        if nrows <= 0 or ncols <= 0:
            raise ValueError("Number of rows and columns must be greater than 0.")
        self.board = [[GameBoardPlayer.NONE for _ in range(ncols)] for _ in range(nrows)]

    def get_nrows(self):
        return(len(self.board))

    def get_ncols(self):
        return (len(self.board[0] if self.board else 0))

    def set(self, row, col, value):
        if not(0 <= row < self.get_nrows()) or not (0 <= col < self.get_ncols()):
            raise IndexError("Row or column out of bounds.")
        self.board[row][col] = value
        

    def get(self, row, col):
        if not(0 <= row < self.get_nrows()) or not (0 <= col < self.get_ncols()):
            raise IndexError("Row or column out of bounds.")
        return self.board[row][col]
        

    def __str__(self):
        board_str = ''
        for row in range(self.get_nrows()):
            # Construct each row
            row_str = ' | '.join(str(self.get(row, col)) for col in range(self.get_ncols()))
            board_str += row_str

            # Add row separator, except after the last row
            if row < self.get_nrows() - 1:
                board_str += '\n' + '--+-' * (self.get_ncols() - 1) + '\n'

        return board_str
    
    def get_winner(self):
        nrows = self.get_nrows()
        ncols = self.get_ncols()

        # Check rows and columns for a winner
        for i in range(nrows):
            if all(self.get(i, j) == self.get(i, 0) != GameBoardPlayer.NONE for j in range(ncols)):
                return self.get(i, 0)
        for j in range(ncols):
            if all(self.get(i, j) == self.get(0, j) != GameBoardPlayer.NONE for i in range(nrows)):
                return self.get(0, j)

        # Check diagonals for a winner (only for square boards)
        if nrows == ncols:
            # Main diagonal
            if all(self.get(i, i) == self.get(0, 0) != GameBoardPlayer.NONE for i in range(nrows)):
                return  self.get(0, 0)
            # Anti-diagonal
            if all(self.get(i, ncols - 1 - i) == self.get(0, ncols - 1) != GameBoardPlayer.NONE for i in range(nrows)):
                return self.get(0, ncols - 1)

        # Check for a draw
        if all(self.get(i, j) != GameBoardPlayer.NONE for i in range(nrows) for j in range(ncols)):
            return GameBoardPlayer.DRAW

        return GameBoardPlayer.NONE  # Return NONE if no winner is found


class BitGameBoard:
    """class that represents a rectangular game board"""

    def __init__(self, nrows, ncols):
        pass

    def get_nrows(self):
        pass

    def get_ncols(self):
        pass

    def set(self, row, col, player):
        pass

    def get(self, row, col):
        pass

    def __str__(self):
        return "(To be implemented)"

    def get_winner(self):
        return GameBoardPlayer.NONE


class TicTacToeBoard:
   
    NROWS = 3
    NCOLS = 3

    def __init__(self):
        # The two game boards can be used interchangeably.
        self.board = ArrayGameBoard(self.NROWS, self.NCOLS)
        # self.board = BitGameBoard(self.NROWS, self.NCOLS)

    def set(self, row, col, value):
        if self.board.get(row, col) != GameBoardPlayer.NONE:
            raise ValueError(f"{row} {col} already has {self.board.get(row, col)}")
        self.board.set(row, col, value)

    def clear(self, row, col):
        self.board.set(row, col, GameBoardPlayer.NONE)

    def get(self, row, col):
        return self.board.get(row, col)

    def get_winner(self):
        return self.board.get_winner()

    def __str__(self):
        return self.board.__str__()


def test_3x3_game_board_positivecheck(gb):
    print("Testing ValueError for instantiation")
    print(gb)
    

def test_3x3_game_board(gb):
    print("Testing IndexError for getter")
    
    print(gb)

    print(f"winner of empty board is '{gb.get_winner()}'")

    gb.set(0, 0, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print(gb)
    gb.set(0, 1, GameBoardPlayer.X)
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print(gb)
    gb.set(0, 2, GameBoardPlayer.X)
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print(gb)
        
  
    print()
    print(f"winner of board with 1 row of X is '{gb.get_winner()}'")

    try:
        gb.get(100, 100)
        print("gb.get(100, 100) fails to raise IndexError")
    except IndexError:
        print("gb.get(100, 100) correctly raises IndexError")

def test_3x3_game_board_draw(gb):
    # Test __str__()
    print("Testing for DRAW and index error on setter")
    print(gb)

    print(f"winner of empty board is '{gb.get_winner()}'")

    gb.set(0, 0, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(1, 1, GameBoardPlayer.O)
    print("gb.get(1, 1) returns", gb.get(1, 1))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(2, 0, GameBoardPlayer.X)
    print("gb.get(2, 0) returns", gb.get(2, 0))
    print(gb)
    print(f"winner of board  is '{gb.get_winner()}'")
    gb.set(1, 1, GameBoardPlayer.O)
    print("gb.get(1, 1) returns", gb.get(1, 1))
    print(gb)
    gb.set(2, 1, GameBoardPlayer.X)
    print("gb.get(2, 1) returns", gb.get(2, 1))
    print(gb)
    gb.set(2, 2, GameBoardPlayer.O)
    print("gb.get(2, 2) returns", gb.get(2, 2))
    print(gb)
    gb.set(1, 2, GameBoardPlayer.X)
    print("gb.get(1, 2) returns", gb.get(1, 2))
    print(gb)     
    gb.set(0, 2, GameBoardPlayer.O)
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print(gb)   
    gb.set(0, 1, GameBoardPlayer.X)
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print(gb) 
    gb.set(1, 0, GameBoardPlayer.O)
    print("gb.get(1, 0) returns", gb.get(1, 0))
    print(gb) 
  
    print()
    
    
    print(f"winner of board is '{gb.get_winner()}'")

    try:
        gb.set(-3, 3, GameBoardPlayer.X)
        print("gb.set(-3, 3, GameBoardPlayer.X) fails to raise IndexError")
    except IndexError:
        print("gb.get(-3, 3, GameBoardPlayer.X) correctly raises IndexError")



def test_3x3_game_board_diagonal(gb):
    # Test __str__()
    print("Testing for DIAGONAL WIN")
    print(gb)

    print(f"winner of empty board is '{gb.get_winner()}'")

    gb.set(0, 0, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(1, 0, GameBoardPlayer.O)
    print("gb.get(1, 0) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(1, 1, GameBoardPlayer.X)
    print("gb.get(1, 1) returns", gb.get(1, 1))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(2, 0, GameBoardPlayer.O)
    print("gb.get(2, 0) returns", gb.get(2, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(2, 2, GameBoardPlayer.X)
    print("gb.get(2, 2) returns", gb.get(2, 2))
    print(gb)
    print()
    print(f"winner of board with 1 diagonal of X is '{gb.get_winner()}'")

def test_4x3_game_board_row_x(gb):
  
    print("Testing for ROW WIN")
    print(gb)

    print(f"winner of empty board is '{gb.get_winner()}'")

    gb.set(0, 1, GameBoardPlayer.X)
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(1, 2, GameBoardPlayer.O)
    print("gb.get(1, 2) returns", gb.get(1, 2))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(2, 0, GameBoardPlayer.X)
    print("gb.get(2, 0) returns", gb.get(2, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(1, 0, GameBoardPlayer.O)
    print("gb.get(1, 0) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(0, 0, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(2, 2, GameBoardPlayer.O)
    print("gb.get(2, 2) returns", gb.get(2, 2))
    print(gb) 
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(0, 2, GameBoardPlayer.X)
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print(gb) 
    print()
    print(f"winner of board with 1 Row of X is '{gb.get_winner()}'")

def test_4x3_game_board_col_o(gb):
    # Test __str__()
    print("Testing for Rectangular COLUMN WIN")
    print(gb)

    print(f"winner of empty board is '{gb.get_winner()}'")

    gb.set(0, 1, GameBoardPlayer.X)
    print("gb.get(0, 1) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(1, 2, GameBoardPlayer.O)
    print("gb.get(1, 2) returns", gb.get(1, 2))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(2, 0, GameBoardPlayer.X)
    print("gb.get(2, 0) returns", gb.get(2, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(0, 2, GameBoardPlayer.O)
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(0, 0, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(2, 2, GameBoardPlayer.O)
    print("gb.get(2, 2) returns", gb.get(2, 2))
    print(gb)   
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(1, 0, GameBoardPlayer.X)
    print("gb.get(1, 0) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(3, 2, GameBoardPlayer.O)
    print("gb.get(3, 2) returns", gb.get(3, 2))
    print(gb) 
    print()
    print(f"winner of rectangular board with 1 Column of O is '{gb.get_winner()}'")

def test_4x3_game_board_for_exceptions(gb):
    # Test __str__()
    print("Testing for COLUMN WIN")
    print(gb)

    print(f"winner of empty board is '{gb.get_winner()}'")

    gb.set(0, 1, GameBoardPlayer.X)
    print("gb.get(0, 1) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(1, 2, GameBoardPlayer.O)
    print("gb.get(1, 2) returns", gb.get(1, 2))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(2, 0, GameBoardPlayer.X)
    print("gb.get(2, 0) returns", gb.get(2, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(0, 2, GameBoardPlayer.O)
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(0, 0, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(2, 2, GameBoardPlayer.O)
    print("gb.get(2, 2) returns", gb.get(2, 2))
    print(gb)  
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(1, 0, GameBoardPlayer.X)
    print("gb.get(1, 0) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(3, 2, GameBoardPlayer.O)
    print("gb.get(3, 2) returns", gb.get(3, 2))
    print(gb) 
    print()
    
    
    print(f"winner of board with 1 Column of O is '{gb.get_winner()}'")


def test_4x3_game_board_for_extreme_case(gb):
    # Test __str__()
    print("Testing for COLUMN WIN")
    print(gb)

    print(f"winner of empty board is '{gb.get_winner()}'")

    gb.set(0, 1, GameBoardPlayer.X)
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(1, 2, GameBoardPlayer.O)
    print("gb.get(1, 2) returns", gb.get(1, 2))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(2, 0, GameBoardPlayer.X)
    print("gb.get(2, 0) returns", gb.get(2, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(0, 2, GameBoardPlayer.O)
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(0, 0, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(2, 2, GameBoardPlayer.O)
    print("gb.get(2, 2) returns", gb.get(2, 2))
    print(gb)   
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(1, 0, GameBoardPlayer.X)
    print("gb.get(1, 0) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(3, 2, GameBoardPlayer.O)
    print("gb.get(3, 2) returns", gb.get(3, 2))
    print(gb) 
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(4, 7, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(5, 8, GameBoardPlayer.O)
    print("gb.get(0, 1) returns", gb.get(1, 2))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(6, 8, GameBoardPlayer.X)
    print("gb.get(0, 2) returns", gb.get(2, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(3, 6, GameBoardPlayer.O)
    print("gb.get(0, 0) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(4, 5, GameBoardPlayer.X)
    print("gb.get(0, 1) returns", gb.get(0, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(2, 7, GameBoardPlayer.O)
    print("gb.get(0, 2) returns", gb.get(2, 2))
    print(gb)  
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(7, 8, GameBoardPlayer.X)
    print("gb.get(0, 1) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(4, 2, GameBoardPlayer.O)
    print("gb.get(0, 2) returns", gb.get(3, 2))
    print(gb) 
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(4, 7, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(5, 2, GameBoardPlayer.O)
    print("gb.get(0, 1) returns", gb.get(1, 2))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(6, 8, GameBoardPlayer.X)
    print("gb.get(0, 2) returns", gb.get(2, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(6, 2, GameBoardPlayer.O)
    print("gb.get(0, 0) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(4, 5, GameBoardPlayer.X)
    print("gb.get(0, 1) returns", gb.get(0, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(7, 2, GameBoardPlayer.O)
    print("gb.get(0, 2) returns", gb.get(2, 2))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")     
    gb.set(7, 8, GameBoardPlayer.X)
    print("gb.get(0, 1) returns", gb.get(1, 0))
    print(gb)
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(8, 2, GameBoardPlayer.O)
    print("gb.get(0, 2) returns", gb.get(3, 2))
    print(gb) 
    print(f"winner of board is '{gb.get_winner()}'")
    gb.set(9, 2, GameBoardPlayer.O)
    print("gb.get(0, 2) returns", gb.get(3, 2))
    print(gb) 
    print()
    
    
    print(f"winner of board with 1 Column of O is '{gb.get_winner()}'")
if __name__ == '__main__':
 ### I created separate test functions to follow output easier
    test_3x3_game_board(ArrayGameBoard(3, 3))
    test_3x3_game_board_draw(ArrayGameBoard(3, 3))
    test_3x3_game_board_diagonal(ArrayGameBoard(3, 3))
    test_4x3_game_board_row_x(ArrayGameBoard(4, 3))
    test_4x3_game_board_col_o(ArrayGameBoard(4, 3))
    test_4x3_game_board_for_exceptions(ArrayGameBoard(4, 3))
    #test_3x3_game_board_positivecheck(ArrayGameBoard(-3, 3))
    
    
  ### this is a 10X10 board, and I tested it works. However
    # It occupied too much space on the output bar.
    # Therefore I will not include it to my run file
    # test_4x3_game_board_for_extreme_case(ArrayGameBoard(10, 9))
    
    # test_3x3_game_board(BitGameBoard(3, 3))
    






