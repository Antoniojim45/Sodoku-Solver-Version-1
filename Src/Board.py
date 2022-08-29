from tkinter import *

class board():
    """
    A class to initalize the board. 

    Attrubutes
    --------------
    tk: obj
        tk is the tkinter object and all the methods that will come
        with it.
    
    board: list
        board is a list of values that act as the values on the 
        sodoku solver board. 

    board_cpy: list
        a copy of the board to keep track of the previous values.
    

    Methods
    --------------
    create_board(board, tk, cells, board_cpy):
        creates the board UI by looping thorught the list, this also builds the board duplicate. 
    """

    def __init__(self, tk, board, board_cpy):
        self.board = board
        self.tk = tk
        cells = {}
        self.board_cpy = board_cpy
        self.create_board(board, tk, cells, board_cpy)

    def create_board(self, board, tk, cells, board_cpy):
        """
        creates the board UI by looping thorught the list, this also builds the board duplicate.

        Parameters
        ---------------
        tk: obj
            tk is the tkinter object and all the methods that will come
            with it.
    
        board: list
            board is a list of values that act as the values on the 
            sodoku solver board. 

        board_cpy: list
            a copy of the board to keep track of the previous values.

        cells: dict
            a dictionary that stores the tkinter object with the particular spot. 
        """

        # create a loop that will create the board blank.
        for row in range(9):
            for column in range(9):
                # Create a single box widget
                cell = Frame(tk, bg='white', highlightbackground='black', highlightcolor='black', highlightthickness= 1)

                if board[row][column] == -1:
                    value = Label(cell, text=" ", font=("Courier", 12), width=4, height=2, padx=3, pady=3)
        
                else:
                    value= Label(cell, text=str(board[row][column]), font=("Courier", 12), width=4, height=2, padx=3, pady=3)


                # store the value widget into a matrix so that we can keep track of the widget placement
                board_cpy[row][column] = value

                # place box the row and the column  
                cell.grid(row=row, column=column)

                # input a tuple onto the cell list and have it equal to the box. 
                cells[(row, column)] = cell

                value.pack()