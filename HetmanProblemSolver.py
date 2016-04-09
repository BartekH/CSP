


def solveHetman(grid, queen):
    if len(grid) == queen:
        print grid
        return True
    for row in range(0,len(grid)):
        if isCorrect(grid, row, queen):
            grid[row, queen] = 1
            if solveHetman(grid, queen + 1):
                return True
            grid[row, queen] = 0
    return False





def isCorrect(grid, row, column):
    return isRowCorrect(grid,row) and  isColumnCorrect(grid, column) and isDiagonalCorrect(grid, row, column)

def isRowCorrect(grid, row):
    for col in range(len(grid)):
        if grid[row, col] == 1:
            return False
    return True

def isColumnCorrect(grid, column):
    for row in range(len(grid)):
        if grid[row, column] == 1:
            return False
    return True


def checkUpperDiagonal(grid, row, column):
    iterRow = row
    iterCol = column
    while iterCol >= 0 and iterRow >= 0:
        if grid[iterRow, iterCol] == 1:
            return False
        iterCol -= 1
        iterRow -= 1
    return True


def checkLowerDiagonal(grid, row, column):
    iterRow = row
    iterCol = column
    while iterCol >= 0 and iterRow < len(grid):
        if grid[iterRow, iterCol] == 1:
            return False
        iterRow += 1
        iterCol -= 1
    return True


def isDiagonalCorrect(grid, row, column):
    return checkUpperDiagonal(grid, row ,column) and checkLowerDiagonal(grid, row, column)



def getActualDomain(grid):
    pass


class ActualDomain:

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash(self.row) ^ hash(self.column)