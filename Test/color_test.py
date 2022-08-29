# Color Test
"""
In this module, we will be testing on how to input color into the grid.
Color will be important to indicate whether the input is valid or not. 
the first test will consist of a single green sqaure moving across the board. 
a second test will consist of going at a certain point of the board as a green square 
then turn red. 

"""

# import the tkinter libary
from tkinter import *
import time


# initalize the tkinter object and window layout
root = Tk()
root.title("Sodoku Solver")
root.geometry("470x430")
cells = {}

# create example board
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

store_value = [[0 for i in range(9)] for j in range(9)]

# create the initial board function
def create_board(board):
    for row in range(9):
        for column in range(9):
            # Create a single box widget
            cell = Frame(root, bg='white', highlightbackground='black', highlightcolor='black', highlightthickness= 1)

            if board[row][column] == -1:
                value = Label(cell, text=" ", font=("Courier", 12), width=4, height=2, padx=3, pady=3)
        
            else:
                value= Label(cell, text=str(board[row][column]), font=("Courier", 12), width=4, height=2, padx=3, pady=3)


            # store the value widget into a matrix so that we can keep track of the widget placement
            store_value[row][column] = value

            # place box the row and the column  
            cell.grid(row=row, column=column)

            # input a tuple onto the cell list and have it equal to the box. 
            cells[(row, column)] = cell

            value.pack()

create_board(example_board)

# store_value[0][0].config(bg = 'green')

# loop through the board with green color
for row in range(9):
    for col in range(9):
        if example_board[row][col] == -1:
            store_value[row][col].config(bg = 'green')
        
        else:
            continue

        root.update()
        time.sleep(0.10)

        store_value[row][col].config(bg = 'white')


time.sleep(1)

for row in range(9):
    for col in range(9):
        if example_board[row][col] == -1:
            store_value[row][col].config(bg = 'red')
        
        else:
            continue

        root.update()
        time.sleep(0.10)

        store_value[row][col].config(bg = 'white')


root.mainloop()