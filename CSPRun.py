import DataProvider
import SudokuSolver
import time


sudoku9x9 = DataProvider.generateSudoku9x9(6)
start = time.time()
solved = SudokuSolver.solve9x9(sudoku9x9)
end = time.time()
print "Time = ", end-start