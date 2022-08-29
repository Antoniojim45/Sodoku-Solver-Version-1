""" Sodoku_Solver_Ver1.py

This is the main function of the project "Sodoku Solver". 
The sodoku solver version 1 is a simple solver that fills in the 
spaces for the user. the algorithm consist of backtracking where the 
program will try out a value and if the value is not satisfactory then 
the program will erase the old choice with a suitable one. 

the project requires'tkinter' to be installed. 
Author: Antonio Jimenez
Version: 1

"""
from Functions import Sodoku_Solver
from tkinter import *
from Board import board
from Stats import Stats

root = Tk()
root.title("Sodoku Solver")
s_settings = Stats()


board(root, s_settings.example_board, s_settings.store_value)
Sodoku_Solver(root, s_settings.example_board, s_settings.store_value)



root.mainloop()