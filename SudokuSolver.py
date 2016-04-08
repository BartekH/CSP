import numpy
import numpy as np
from operator import or_

sudokuSize = 9




def solve9x9Backtracking(grid, counter=0):
    row, column = findUnassignedPlaces(grid)
    counter += 1
    if row == -2 and column == -2:
        showSolvedGrid(grid)
        return True  # solution found!
    actualDomain = getActualDomain(grid, row, column)
    for proposedNumber in actualDomain:
        if isCorrect(grid, row, column, proposedNumber):
            grid[row,column] = proposedNumber

            if solve9x9Backtracking(grid,counter):
                return True
            grid[row,column] = 0
    return False


def forwardCheck(grid, row, column): # return False if does not have a conflict
    loopIter = True
    tempGrid = grid.copy()
    while loopIter:
        row, column = findUnassignedPlaces(tempGrid)
        if row == -2 and column == -2:
            return False
        actualDomain = getActualDomain(tempGrid, row,column)
        if actualDomain == []:
            return True
        else:
            tempGrid[row,column] = actualDomain[0]




def solve9x9ForwardChecking(grid):
    row, column = findUnassignedPlaces(grid)
    if row == -2 and column == -2:
        showSolvedGrid(grid)
        return True  # solution found!
    actualDomain = getActualDomain(grid, row, column)
    for proposedNumber in actualDomain:
        if isCorrect(grid, row, column, proposedNumber):
            grid[row,column] = proposedNumber
            if forwardCheck(grid, row, column):
                grid[row, column] = 0
            if solve9x9ForwardChecking(grid):
                return True
            grid[row,column] = 0
    return False





def solve9x9ForwardCheckingNew(grid, counter=0):
    counter += 1
    row, column = findUnassignedPlaces(grid)
    if row == -2 and column == -2 :
        showSolvedGrid(grid)
        return True  # solution found!
    actualDomain = getActualDomain(grid, row, column)
    for proposedNumber in actualDomain:
        grid[row,column] = proposedNumber
        domainWipeOut = False
        for variable in getUnassignedFromConstraints(grid.copy(), row, column):
            if fc(variable.grid, variable.row, variable.column):
                domainWipeOut = True
                break
        if not domainWipeOut:
            solve9x9ForwardCheckingNew(grid, counter)

        grid[row,column] = 0


def getUnassignedInRow(grid, row):
    result = []
    columnCounter = -1
    for variable in grid[row]:
        columnCounter += 1
        if variable == 0:
            result.append(UnassignedVariableFromConstrain(row, columnCounter, grid.copy()))
    return set(result)


def getUnassignedInColumn(grid, column):
    result = []
    rowCounter = -1
    for variable in grid[:,column]:
        rowCounter += 1
        if variable == 0:
            result.append(UnassignedVariableFromConstrain(rowCounter, column, grid.copy()))
    return set(result)


def getUnassignedInSquare(grid, rowStart, columnStart):
    result = []
    if rowStart == 0:
        rowStart = 1
    if columnStart == 0:
        columnStart = 1
    for row in range(0,3):
        for col in range(0,3):
            if grid[rowStart+row,columnStart+col] == 0:
                result.append(UnassignedVariableFromConstrain(row+rowStart, col+columnStart, grid.copy()))
    return set(result)


def getUnassignedFromConstraints(grid, row, column):
    unassignedInRow = getUnassignedInRow(grid,row)
    unassignedInColumn = getUnassignedInColumn(grid, column)
    unassignedInSquare = getUnassignedInSquare(grid, row - row%3, column - column%3)
    unassigneds = unassignedInSquare.symmetric_difference(unassignedInColumn)
    unassigneds = unassigneds.symmetric_difference(unassignedInRow)
    return unassigneds


def fc(grid, row, column):
    actualDomain = getActualDomain(grid, row, column)
    domainCopy = list(actualDomain)
    for domainProposition in actualDomain:
        if not isCorrect(grid, row, column, domainProposition):
            domainCopy.remove(domainProposition)
    return len(domainCopy) == 0





def getActualDomain(grid, row, column):
    resultList = set(range(1,10))
    wholeRow = set(grid[row,:])- set([0])
    wholeColumn = set(grid[:,column])- set([0])
    wholeSquare = getSquare(grid, row - row%3, column - column%3) - set([0])
    reducedEliminatedSet = reduce(or_, [wholeRow, wholeColumn, wholeSquare])
    resultList = resultList.symmetric_difference(reducedEliminatedSet)
    return list(resultList)

def getSquare(grid, row, column):
    squareDomain = []
    tempIter = 1
    for tempRow in range(row, row+3):
        for tempCol in range(column, column+3):
            squareDomain.append(grid[tempRow, tempCol])
    return set(squareDomain)




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


class UnassignedVariableFromConstrain:

    def __init__(self, row, column, grid):
        self.row = row
        self.column = column
        self.grid = grid

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash(self.row) ^ hash(self.column)
