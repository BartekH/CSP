import DataProvider
import SudokuSolver
import HetmanProblemSolver
import time
import csv

from Tkinter import Tk
from GUI import SudokuUI
from GUI import App

# start = time.time()
# solved = SudokuSolver.solve9x9Backtracking(DataProvider.sudoku9x9Normal)
# solved = SudokuSolver.solve9x9ForwardCheckingCLI(DataProvider.sudoku9x9Normal)
#solved = HetmanProblemSolver.solveHetmanForwardCheckingHeuristic(DataProvider.getHetmanGrid(8), 0)
# solved = HetmanProblemSolver.solveHetmanBacktracking(DataProvider.getHetmanGrid(15),0)
# print solved
# end = time.time()
# print "Time = ", end - start
# import numpy as np
# import matplotlib.pyplot as plt

def runTestsHetmans(N):
    timeResults = []
    for n in range(8,N):
        start = time.time()
        solved = HetmanProblemSolver.solveHetmanForwardChecking(DataProvider.getHetmanGrid(n),0)
        end = time.time()
        timeResults.append(end-start)
        print "iteration number", n
    f = open("HetmanForwardBEZZHeuryProba23Wielkosc.csv", 'wb')
    try:
        # plt.plot(timeResults, range(8,N))
        # plt.axis([0,30,8,25])
        # plt.show()
        writer = csv.writer(f)
        writer.writerow( ('wielkosc szachownicy', 'czas') )
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
            solved = SudokuSolver.solve9x9Backtracking(DataProvider.generateSudoku16x16(n))
            end = time.time()
            timeResults.append(end-start)
    f = open("Pop_Sudoku16_Back_bezHeur.csv", 'wb')
    try:
        # plt.plot(timeResults, range(8,N))
        # plt.axis([0,30,8,25])
        # plt.show()
        writer = csv.writer(f)
        writer.writerow( ('ilosc elementow', 'czas') )
        for n in range(32):
            writer.writerow( (n+1, timeResults[n]) )
    finally:
        f.close()
    print "finished"

#runTestSudoku(256)
start=time.time()
solved = SudokuSolver.solve9x9BacktrackingHeuritic(DataProvider.generateSudoku16x16(80))
end=time.time()
print "time = ", end-start
