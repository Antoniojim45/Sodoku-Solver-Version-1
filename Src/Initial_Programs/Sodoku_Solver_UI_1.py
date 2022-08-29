"""
Sodoku Solver UI

In this file we will be using the sodoku solver algorithm and construct
a user interface so that the method of the sodoku solver with back tracking
can be presented. 


"""
from tkinter import *
import time

from matplotlib.pyplot import text

root = Tk()
root.title("Sodoku Solver")
root.geometry("470x430")
cells = {}
store_value = [ [0 for i in range(9)] for j in range(9) ]

example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],xz

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

# Define the Board
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

def solve_sodoku(puzzle):
    """
    solving sodoku using a backtracking technique. we will be passing in a 
    list of list, where each inner list is a row in the sodoku board. 
    Return whether a solution exists.mutates puzzle to be the solution 
    (if the solution exists)


    Parameters
    ----------------
    puzzle: list
        puzzle is a 2 dimentional list, with -1 acting as empty spaces.

    """
    
    # Step 1: choose somewhere in the puzzle to make a guess. 
    row, col = find_next_empty(puzzle)


    # step 1.1: if there is nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1,10) is 1, 2, 3, ... 9
        # step 3: check if this is valid guess 
        if is_valid(puzzle, guess, row, col):

            # step 3.1: if this is valid, then place that guess on the puzzle!
            # change the color to green meaning its valid
            store_value[row][col].config(bg = 'green')
            puzzle[row][col] = guess

            # change the text to the guess
            store_value[row][col].config(text = str(guess))

            root.update()
            time.sleep(0.00001)

            # now recurse using this puzzle !
            # step 4: recursively call or function
            if solve_sodoku(puzzle):
                return True
            
        # step 5: if not valid OR if our guess does not solve the puzzle, then we need to 
        #         backtrack and try a new number. 
        puzzle[row][col] = -1
        
        # change the UI to a blank and red
        store_value[row][col].config(text = ' ')
        store_value[row][col].config(bg = 'red')

        # update
        root.update()
        time.sleep(0.00001)

        store_value[row][col].config(bg = 'white')


    # Step 6: if none of the numbers work then this puzzle is unsolvable.
    return False

def is_valid(puzzle, guess, row, col):
    """
    is_valid checks whether guessed number is valid within the space. 

    Parameters
    ------------
    puzzle: list
        puzzle is a 2 dimentional list, with -1 acting as empty spaces.
    
    guess: int
        guess is a integer that will be placed in the space. if the number is 
        valid then the value will be placed there. 
    
    row: int
        the row where the guess will inhabit on the board.

    col: int
        the column that the guess will inhabit on the board. 

    """
    # figure out whether the guess at the row/col of the puzzle is a valid guess
    # return True if is valid, false otherwise

    # lets start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # now the columns
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)] # shorter version

    if guess in col_vals:
        return False

    # and then the square 
    # this is tricky, but we want to get where the 3x3 square starts
    # and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3 # 1 // 3 = 0, 5 // 3 = 1, ...
    col_start = (col // 3) * 3 

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # if we get here, these checks pass
    return True

def find_next_empty(puzzle):
    """
    find the next row, col on the puzzle that's not filled yet --> rep with -1
    return row, col tuple (or (None, None) id there is none)

    Parameters
    -------------
    puzzle: 
        puzzle is a 2 dimentional list, with -1 acting as empty spaces.
    
    """

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:

                # turn the spot red (meaning its under works)
                store_value[r][c].config(bg='red')
                return r, c
    
    return None, None # if there is no spaces in the puzzle are empty (-1)



# main function
def main(board):
    create_board(board)
    solve_sodoku(board)


main(example_board)

root.mainloop()