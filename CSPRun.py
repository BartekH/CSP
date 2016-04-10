import DataProvider
import SudokuSolver
import HetmanProblemSolver
import time
from Tkinter import Tk
from GUI import SudokuUI
from GUI import App

#
# sudoku9x9 = DataProvider.sudoku9x9Normal
# root = Tk()
# frame = SudokuUI(root, sudoku9x9)
# app = App(frame)



# rowCounter = 0
# columnCounter=0
# for r in range(9):
#     for c in range(9):
#         tk.Label(root, text='%s   '%sudoku9x9[r,c],
#             borderself.WIDTH=1 ).grid(row=rowCounter,column=columnCounter)
#         columnCounter += 1
#     columnCounter = 0
#     rowCounter += 1
# root.mainloop()

start = time.time()
#solved = SudokuSolver.solve9x9Backtracking(DataProvider.sudoku9x9Normal)
solved = SudokuSolver.solve9x9ForwardCheckingCLI(DataProvider.sudoku9x9Normal)
#solved = HetmanProblemSolver.solveHetmanForwardChecking(DataProvider.getHetmanGrid(8), 0)
#solved = HetmanProblemSolver.solveHetmanBacktracking(DataProvider.getHetmanGrid(8), 0)
print solved
end = time.time()
print "Time = ", end-start

