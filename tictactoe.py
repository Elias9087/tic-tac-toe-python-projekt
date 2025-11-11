############################################################################
# Filename: tictactoe.py
# Description: A simple Tic Tac Toe game using Tkinter
# Author: Elias Huber
# Date: 2025-11-11
############################################################################
import tkinter as tk  

# Create the main window
root = tk.Tk()  
root.resizable(False, False)  # prevent window resizing
root.title("Tic Tac Toe")  # set window title

# Add title label
tk.Label(root, text="Tic Tac Toe", font=('Ariel', 25)).pack()
current_chr = "X"

# Create play area
play_area = tk.Frame(root, width=300, height=300, bg='white')  

# Lists to store which points are taken by X and O
X_points = [] # List of X points
O_points = [] # List of O points

# Define a class for each button in grid
class XOPoint:  
    def __init__(self, x, y):
        # Grid coordinates
        self.x = x  
        self.y = y  
        # initially no symbol is placed
        self.value = None  

        # Create button
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)

        # Place button in grid
        self.button.grid(row=x, column=y)

    # Method to set X or O on button
    def set(self):
        global current_chr

        # Only set if button is not already taken
        if not self.value:
            self.button.configure(text=current_chr, bg='snow', fg='black')
            # Store the symbol in the object
            self.value = current_chr 

            # Add this point to the respective list
            if current_chr == "X":
                X_points.append(self)
                current_chr = "O" # Switch turn to O
            elif current_chr == "O":
                O_points.append(self)
                current_chr = "X" # Switch turn to X

            # After every move, check for a win
        check_win()

    # reset cell
    def reset(self):  
        self.button.configure(text="", bg='white')  
        self.value = None

# Create 3x3 grid of XOPoint objects
for x in range(1, 4):
    for y in range(1, 4):
        XOPoint(x, y) # create a button for each grid position

# Class to represent a winning possibility       
class WinningPossibility:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Store the three coordinates that form a winning line
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    # Check if a player has satisfied this winning possibility
    def check(self, for_chr):
        p1_satisfied = False
        p2_satisfied = False
        p3_satisfied = False

        # Check for X
        if for_chr == 'X':
            for point in X_points:
                # Check if the point matches any of the winning line coordinates
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        
        # Check for O
        elif for_chr == 'O':
            for point in O_points:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        # Return True if all three positions are satisfied
        return all([p1_satisfied, p2_satisfied, p3_satisfied])

# Define all 8 possible winning combinations
winning_possibilities = [
    WinningPossibility(1, 1, 1, 2, 1, 3), # top row
    WinningPossibility(2, 1, 2, 2, 2, 3), # middle row
    WinningPossibility(3, 1, 3, 2, 3, 3), # bottom row
    WinningPossibility(1, 1, 2, 1, 3, 1), # left column
    WinningPossibility(1, 2, 2, 2, 3, 2), # middle column
    WinningPossibility(1, 3, 2, 3, 3, 3), # right column
    WinningPossibility(1, 1, 2, 2, 3, 3), # diagonal main
    WinningPossibility(3, 1, 2, 2, 1, 3)  # anti diagonal
]

# Function to check for a win after each move
def check_win():
    for possibility in winning_possibilities:
        # Check all combinations for X
        if possibility.check('X'):
            print("X won!")
            return
        # Check all combinations for O
        elif possibility.check('O'):
            print("O won!")
            return
play_area.pack(pady=10, padx=10)  

root.mainloop()