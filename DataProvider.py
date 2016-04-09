import numpy as np
from random import randint



sudoku9x9 = np.matrix([[3, 1, 6, 5, 7, 8, 4, 9, 2]
                          , [5, 2, 9, 1, 3, 4, 7, 6, 8]
                          , [4, 8, 7, 6, 2, 9, 5, 3, 1]
                          , [2, 6, 3, 4, 1, 5, 9, 8, 7]
                          , [9, 7, 4, 8, 6, 3, 1, 2, 5]
                          , [8, 5, 1, 7, 9, 2, 6, 4, 3]
                          , [1, 3, 8, 9, 4, 7, 2, 5, 6]
                          , [6, 9, 2, 3, 5, 1, 8, 7, 4]
                          , [7, 4, 5, 2, 8, 6, 3, 1, 9]])

sudoku9x9Normal = np.array([[0, 0, 0, 0, 0, 8, 4, 9, 2]
                          , [5, 2, 0, 1, 3, 4, 7, 6, 8]
                          , [4, 0, 0, 0, 0, 9, 5, 3, 1]
                          , [2, 0, 3, 4, 1, 0, 0, 8, 7]
                          , [0, 0, 4, 0, 0, 0, 1, 2, 5]
                          , [8, 5, 1, 7, 9, 2, 6, 4, 3]
                          , [0, 3, 0, 0, 4, 0, 2, 5, 6]
                          , [6, 9, 0, 0, 0, 0, 8, 7, 4]
                          , [7, 4, 5, 2, 8, 6, 0, 0, 0]])
sudoku9x9Hard = np.array([[4,0,0,0,0,0,8,0,5],
[0,3,0,0,0,0,0,0,0],
[0,0,0,7,0,0,0,0,0],
[0,2,0,0,0,0,0,6,0],
[0,0,0,0,8,0,4,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,6,0,3,0,7,0],
[5,0,0,2,0,0,0,0,0],
[1,0,4,0,0,0,0,0,0]]   )

def generateSudoku9x9(numberOfFields):
    grid = np.zeros(shape = (9,9), dtype=int)
    for iter in range(0,numberOfFields):
        row = randint(0,8)
        col = randint(0,8)
        grid[row, col] = sudoku9x9[row,col]
    return grid


def getHetmanGrid(N):
    return np.array(np.zeros(shape = (N,N), dtype=int))