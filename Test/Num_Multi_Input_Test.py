# Num_Input_test
"""
In this test, we will be testing/researching how to create a backtracking 
animation after placing the values on the sudoku board. The goal is to place 
values dynamically to see how backtracking works. 

"""

# import tkinter
from tkinter import *
import time

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

store_value = [ [0 for i in range(9)] for j in range(9) ]

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

for row in range(9):
    for col in range(9):
        if example_board[row][col] == -1:
            # change the widget text to something else
            store_value[row][col].config(text= '3')

            # change the spot on the array to the same value
            example_board[row][col] = 3
        
        else:
            continue
        
        # update the board
        root.update()
        time.sleep(0.5)


# reverse the loop so that we go backwards. 
for row in reversed(range(9)):
    for col in reversed(range(9)):

        # take a look at the original board so that we know what use to be an empty space. 
        if temp_board[row][col] == -1:

            # change the text in each widget stored in the store value. 
            store_value[row][col].config(text = ' ')

            # revert the spot to a negative one. 
            example_board[row][col] = -1

        
        else:
            continue

        root.update()
        time.sleep(0.5)




root.mainloop()
