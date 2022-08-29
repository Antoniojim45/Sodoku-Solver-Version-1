# Numgrid_test
"""
In this module, we will be testing/researching on how to ipnut values within 
the grid made. using the example board array, the goal is to place the values in their 
respected places, while showing blank lines for places that have a -1. 

"""
from tkinter import *


root = Tk()
root.title("Sodoku Solver")
root.geometry("470x430")


example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

cells = {}


# create the cells, where the numbers will be stored
for row in range(9):
    for column in range(9):
        # Create a single box widget
        cell = Frame(root, bg='white', highlightbackground='black', highlightcolor='black', highlightthickness= 1)

        if example_board[row][column] == -1:
            value = Label(cell, text=" ", font=("Courier", 12), width=4, height=2, padx=3, pady=3)
        
        else:
            value = Label(cell, text=str(example_board[row][column]), font=("Courier", 12), width=4, height=2, padx=3, pady=3)
        
        # place box the row and the column 
        cell.grid(row=row, column=column)

        # input a tuple onto the cell list and have it equal to the box. 
        cells[(row, column)] = cell

        value.pack()






root.mainloop()