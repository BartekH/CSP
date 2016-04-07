import DataProvider
import SudokuSolver
import time


sudoku9x9 = DataProvider.generateSudoku9x9(6)
start = time.time()
#solved = SudokuSolver.solve9x9Backtracking(sudoku9x9)
solved = SudokuSolver.solve9x9ForwardCheckingNew(DataProvider.sudoku9x9Normal)
end = time.time()
print "Time = ", end-start