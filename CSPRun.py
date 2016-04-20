import DataProvider
import SudokuSolver
import NQueensSolver
import time
import csv



def runTestsNQueens(N):
    timeResults = []
    for n in range(8,N):
        start = time.time()
        solved = NQueensSolver.solveNQueensForwardChecking(DataProvider.getHetmanGrid(n), 0)
        end = time.time()
        timeResults.append(end-start)
        print "iteration number", n
    f = open("--.csv", 'wb')
    try:
        # plt.plot(timeResults, range(8,N))
        # plt.axis([0,30,8,25])
        # plt.show()
        writer = csv.writer(f)
        writer.writerow( ('size', 'time') )
        for n in range(1,N-7):
            writer.writerow( (n+7, timeResults[n-1]) )
    finally:
        f.close()
    print "finished"

def runTestSudoku(N):
    timeResults = []
    for n in range(1,N):
        if n%8 == 0:
            print "iter ", n
            start = time.time()
            solved = SudokuSolver.solveBacktracking(DataProvider.generateSudoku16x16(n))
            end = time.time()
            timeResults.append(end-start)
    f = open("--.csv", 'wb')
    try:
        writer = csv.writer(f)
        writer.writerow( ('number of elements', 'time') )
        for n in range(32):
            writer.writerow( (n+1, timeResults[n]) )
    finally:
        f.close()
    print "finished"


start=time.time()
solved = SudokuSolver.solveBacktrackingHeuritic(DataProvider.generateSudoku16x16(10))
end=time.time()
print "time = ", end-start
