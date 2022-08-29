# Grid Test
# Create a 9x9 grid using tkinter and the grid system. 
"""
.geometry(): 
    This method is used to set the dimensions of the Tkinter window and is used to set the 
    position of the main window on the users desktop.

Frame():
    A frame is a widget that displays as a simple rectangle. Typically, you use a frame to 
    organize other widgets both visually and at the coding level.

    essentailly you can have other widgets within the frame. in this case you can have 
    numbers within each box.


grid():
    The grid geometry manager uses the concepts of rows and columns to arrange the widgets.


"""

# Import all the tkinter
from tkinter import *

root = Tk()
root.title("Sodoku Solver") # create the title
root.geometry('455x455') # Creates the geometry of the window 

# create all the main containers.
cells = {}

# create the cells, where the numbers will be stored
for row in range(9):
    for column in range(9):
        # Create a single box widget
        cell = Frame(root, bg='white', highlightbackground='black', highlightcolor='black', highlightthickness= 1, width=50, height=50, padx=3, pady=3)

        # place box the row and the column 
        cell.grid(row=row, column=column)

        # input a tuple onto the cell list and have it equal to the box. 
        cells[(row, column)] = cell



# execute the code
root.mainloop()

