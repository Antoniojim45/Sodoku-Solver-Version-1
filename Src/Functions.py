""" Function.py

In this File the functions will define the sodoku solver algorithm.
This class contains all the methods needed to solve sodoku on a command line
level. 



"""

from tkinter import *
from Animations import animations

        
class Sodoku_Solver():
    """
    A class will represent the sodoku solver algorithm.

    Attributes
    -----------
    tk: obj
        tk is the tkinter object and all the methods that will come
        with it. 

    board: list
        board is a list of values that act as the values on the 
        sodoku solver board. 

    board_cpy: list
        a copy of the board to keep track of the previous values. 


    methods
    ----------
    solve_sodoku(tk, board, board_cpy)
        the main function of the algorithm which uses all the 
        other functions in order to return it to the main function.
    
    is_valid(board, guess, guess, row, col)
        checks if the spot chosen is valid, returns a bool depending on 
        the outcome. 
    
    find_next_empty(board):
        finds the next empty spot on the board. 
        

    """
    def __init__(self, tk, board, board_cpy):
        """
        Parameters
        ------------
        tk: obj
            tk is the tkinter object and all the methods that will come
            with it. 

        board: list
            board is a list of values that act as the values on the 
            sodoku solver board. 

        board_cpy: list
            a copy of the board to keep track of the previous values.
        """
        self.tk = tk
        self.board = board
        self.board_cpy = board_cpy
        self.solve_sodoku(tk, board, board_cpy)
    
    def solve_sodoku(self, tk, board, board_cpy):
        """
        the main method of the sodoku solver algorithm. makes a guess on an 
        empty spot then recurse until there is no spaces left. if the spot is not valid 
        then return the spot to blank. "-1" then return false. 

        Parameters
        --------------
        tk: obj
            the tkinter object and all the methods that will come
            with it.
        
        board: list
            board is a list of values that act as the values on the 
            sodoku solver board.
        
        board_cpy: list
            a copy of the board to keep track of the previous values. 
        
        """
        row, col = self.find_next_empty(board)

        if row is None:
            return True
        
        for guess in range(1, 10):
            # step 3: check if this is valid guess 
            if self.is_valid(board, guess, row, col):

                # step 3.1: if this is valid, then place that guess on the board!
                # change the color to green meaning its valid
                animations.found_number(self, tk, guess, board_cpy, row, col)

                board[row][col] = guess

                # now recurse using this board !
                # step 4: recursively call or function
                if self.solve_sodoku(tk, board, board_cpy):
                    return True
            
        # step 5: if not valid OR if our guess does not solve the board, then we need to 
        #         backtrack and try a new number. 
        board[row][col] = -1
        
        animations.invalid_input(self, tk, board_cpy, row, col)

        # Step 6: if none of the numbers work then this board is unsolvable.
        return False
    
    def is_valid(self, board, guess, row, col):
        """
        figure out whether the guess at the row/col of the board is a valid guess
        return True if is valid, false otherwise

        Parameters
        -------------
        board: list
            board is a list of values that act as the values on the 
            sodoku solver board.

        guess: int
            the guessed number for a particular spot on the board. 
        
        row: int
            the row on the board. 

        col: int 
            the column on the board. 
        """

        # lets start with the row:
        row_vals = board[row]
        if guess in row_vals:
            return False
    
        # now the columns
        # col_vals = []
        # for i in range(9):
        # col_vals.append(board[i][col])
        col_vals = [board[i][col] for i in range(9)] # shorter version

        if guess in col_vals:
            return False

        # and then the square 
        # this is tricky, but we want to get where the 3x3 square starts
        # and iterate over the 3 values in the row/column
        row_start = (row // 3) * 3 # 1 // 3 = 0, 5 // 3 = 1, ...
        col_start = (col // 3) * 3 

        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if board[r][c] == guess:
                    return False

        # if we get here, these checks pass
        return True
    
    def find_next_empty(self, board):
        """
        finds the next empty space on the board. 

        Parameters
        -------------
        board: list
            board is a list of values that act as the values on the 
            sodoku solver board. 
        """
        # keep in mind that we are using 0-8 for our indices
        for r in range(9):
            for c in range(9): # range(9) is 0, 1, 2, ... 8
                if board[r][c] == -1:
                    return r, c
    
        return None, None # if there is no spaces in the puzzle are empty (-1)
