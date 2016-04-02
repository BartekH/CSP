import numpy
sudokuSize = 9




def solve9x9(grid):
    row, column = findUnassignedPlaces(grid)
    if row == -2 and column == -2:
        showSolvedGrid(grid)
        return True  # solution found!

    for proposedNumber in range(1, sudokuSize+1):
        if isCorrect(grid, row, column, proposedNumber):
            grid[row,column] = proposedNumber

            if solve9x9(grid):
                return True
            grid[row,column] = 0
    return False


def findUnassignedPlaces(grid):
    for row in range(0, sudokuSize):
        for col in range(0, sudokuSize):
            if grid[row, col] == 0:
                return row, col
    return -2, -2


def isCorrect(grid, row, column, proposedNumber):
    return isCorrectInRow(grid, row, proposedNumber) \
           and isCorrectInColumn(grid, column, proposedNumber) \
           and isCorrectInBox(grid, row - row%3, column - column%3, proposedNumber)



def isCorrectInRow(grid, row,  proposedNumber):
    for col in range(0, sudokuSize):
        if grid[row,col] == proposedNumber:
            return False
    return True


def isCorrectInColumn(grid,  column, proposedNumber):
    for row in range(0, sudokuSize):
        if grid[row,column] == proposedNumber:
            return False
    return True


def isCorrectInBox(grid, rowStart, columnStart, proposedNumber):
    for row in range(0,3):
        for col in range(0,3):
            if grid[rowStart+row,columnStart+col] == proposedNumber:
                return False
    return True

def showSolvedGrid(grid):
    print grid
