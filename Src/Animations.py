from tkinter import *
import time

class animations():
    """
    a class to store all the animations for the sodoku solver program. 

    Attributes
    ------------
    tk: obj
        tk is the tkinter object and all the methods that will come
        with it.
    """
    def __init__(self, tk):
        self.tk = tk

    def update_screen(self, tk):
        """
        a function to update the screen every set amount of seconds.

        Parameters
        ------------
        tk: obj
            tk is the tkinter object and all the methods that will come
            with it.
        """
        tk.update()
        time.sleep(0.00001) # pause the program for a set amount of seconds. 

    def found_number(self, tk, guess, board_cpy, row, col):
        """
        If the program has found a valid number then change the 
        spot on the board to green. change the board text to the guessed value.

        Parameters
        -----------
        tk: obj
            tk is the tkinter object and all the methods that will come
            with it.

        guess: int
            he guessed number for a particular spot on the board.

        board_cpy: list
            a copy of the board to keep track of the previous values.

        row: int
            the row on the board.

        col: int
            the column on the board. 

        """
        # change the color to green meaning its valid
        board_cpy[row][col].config(bg = 'green')
        # change the text to the guess
        board_cpy[row][col].config(text = str(guess))

        animations.update_screen(self, tk)

    def invalid_input(self, tk, board_cpy, row, col):
        """
        If the input is invalid then the spot on the board will be red and the 
        value on that spot will be erased. 

        Parameters
        -------------
        tk: obj
            the tkinter object and all the methods that will come
            with it.

        board_cpy: list
            a copy of the board to keep track of the previous values. 

        row: int
            the row on the board.

        col: int
            the column on the board. 
        """
        # change the UI to a blank and red
        board_cpy[row][col].config(text = ' ')
        board_cpy[row][col].config(bg = 'red')

        # update
        animations.update_screen(self, tk)

        board_cpy[row][col].config(bg = 'white')