

# ---------------------- N queens methods ----------------------------
def solveHetmanBacktracking(grid, queen):
    if len(grid) == queen:
        print grid
        return True
    rowsProposition = getRowsProposition(grid, queen)
    for row in rowsProposition:
        if isCorrect(grid, row, queen):
            grid[row, queen] = 1
            if solveHetmanBacktracking(grid, queen + 1):
                return True
            grid[row, queen] = 0
    return False

def solveHetmanBacktrackingHeuristic(grid, queen):
    if len(grid) == queen:
        print grid
        return True
    rowsProposition = getHeuristicRowsProposition(grid, queen)
    for row in rowsProposition:
        if isCorrect(grid, row.row, queen):
            grid[row.row, queen] = 1
            if solveHetmanBacktracking(grid, queen + 1):
                return True
            grid[row.row, queen] = 0
    return False


def solveHetmanForwardChecking(grid, queen):
    if len(grid) == queen:
        print grid
        return True
    rowsProposition = getRowsProposition(grid, queen)
    for row in rowsProposition:
        grid[row, queen] = 1
        domainWipeOut = False
        for variable in getUnassignedFromConstraint(grid, queen):
            if fc(grid, variable.row, variable.column):
                domainWipeOut = True
                break
        if not domainWipeOut:
             if solveHetmanForwardChecking(grid, queen+1):
                 return True
        grid[row, queen] = 0

def solveHetmanForwardCheckingHeuristic(grid, queen):
    if len(grid) == queen:
        print grid
        return True
    rowsProposition = getHeuristicRowsProposition(grid, queen)
    for row in rowsProposition:
        grid[row.row, queen] = 1
        domainWipeOut = False
        for variable in getUnassignedFromConstraint(grid, queen):
            if fc(grid, variable.row, variable.column):
                domainWipeOut = True
                break
        if not domainWipeOut:
             if solveHetmanForwardCheckingHeuristic(grid, queen+1):
                 return True
        grid[row.row, queen] = 0

# -------------------------- utils methods --------------------------------

def getRowsList(grid, column):
    rowsProposition = getRowsProposition(grid, column)

def getBestColumn(grid):
    bestColumn = 0
    bestRowsProposition = 0
    for col in range(len(grid)):
        rowsProposition = getRowsProposition(grid, col)
        if len(rowsProposition) >= bestRowsProposition:
            bestRowsProposition = len(rowsProposition)
            bestColumn = col
    return bestColumn

def getUnassignedFromConstraint(grid, queen):
    result = []
    for row in range(len(grid)):
        for col in range(queen+1, len(grid)):
            if grid[row,col] == 0 and isCorrect(grid, row, col):
                result.append(Unassigned(row, col))
    return result


def fc(grid, row, queen):
    actualDomain = getRowsProposition(grid, queen)
    tempDomain = list(actualDomain)
    for propositionRow in actualDomain:
        if not isCorrect(grid, propositionRow, queen):
            tempDomain.remove(propositionRow)
    return len(tempDomain) == 0



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



def getRowsProposition(grid, queen):
    rows = []
    for row in range(len(grid)):
        if isCorrect(grid, row, queen):
            rows.append(row)
    return rows

def getHeuristicRowsProposition(grid, queen):
    rows = []
    for row in range(len(grid)):
        if isCorrect(grid, row, queen):
            tempGrid = grid.copy()
            tempGrid[row,queen] = 1
            rows.append(HeuristicRow(row, queen, rateForHeuristic(tempGrid, queen+1)))
    rows.sort(key=lambda x: x.rate)
    return rows

def rateForHeuristic(grid, queen):
    return len(getRowsProposition(grid, queen))

# -------------------------------- utils classes -----------------------------------

class HeuristicRow:

    def __init__(self, row, column, rate):
        self.row = row
        self.column = column
        self.rate = rate

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash(self.row) ^ hash(self.column)

class Unassigned:

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash(self.row) ^ hash(self.column)