# Num_Input_test
"""
In this test we will be testing/researching on how to create a backtracking 
animation after placing the values in the sodoku board. The goal is dynamically place 
values so that we can see how backtracking works. 

"""

# import tkinter
from tkinter import *

root = Tk()
root.title("Sodoku Solver")
root.geometry("470x430")
cells = {}

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

temp_board = [
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


# first we will create the function that will intitalize the board
def create_board(board):

    for row in range(9):
        for column in range(9):
            # Create a single box widget
            cell = Frame(root, bg='white', highlightbackground='black', highlightcolor='black', highlightthickness= 1)

            if board[row][column] == -1:
                value = Label(cell, text=" ", font=("Courier", 12), width=4, height=2, padx=3, pady=3)
        
            else:
                value = Label(cell, text=str(board[row][column]), font=("Courier", 12), width=4, height=2, padx=3, pady=3)
        
            # place box the row and the column  
            cell.grid(row=row, column=column)

            # input a tuple onto the cell list and have it equal to the box. 
            cells[(row, column)] = cell

            value.pack()



# create the intial example board
create_board(example_board)

# start a for loop that goes through the entire board.
for row in range(9):
    for col in range(9):
        if example_board[row][col] == -1:
            example_board [row][col] = 3
        
        else:
            continue

        root.update()
        root.after(200, create_board(example_board))



# create a loop that will go backwards from the list
# creata a reverse board


for row in reversed(range(9)):
    for col in reversed(range(9)):
        if temp_board[row][col] == -1:
            example_board[row][col] = " "
        
        else:
            continue

        root.update()
        root.after(200, lambda:create_board(example_board))


# place the first number on the board. 
# use sleep as a pause. 
# go to the next space.
# if there is a number there already then leave it alone.
# if there is no number then place a number in there. 
# keep going until you reach the end of the file. 




root.mainloop()



