
sudokuSize = 9




def solve9x9(grid):

    row = 0;column = 0

    row, column = findUnassignedPlaces(grid)
    if(row == -2 and column == -2):
        return True #solution found!

    for proposedNumber in range(1,sudokuSize):
        if(isCorrect(grid, ))


def findUnassignedPlaces(grid):
    for row in range(1, sudokuSize):
        for col in range(1, sudokuSize):
            if grid[row, col] == 0:
                return row, col
    return -2, -2

def isCorrect(grid):
    pass
