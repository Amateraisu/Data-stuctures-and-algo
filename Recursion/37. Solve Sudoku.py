class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solvePartialSudoku(0,0,board)
            
        return 
    
    
    
def solvePartialSudoku(row, column, board):
    currentRow = row 
    currentColumn = column 
    
    if currentColumn == len(board[0]):
        currentRow += 1 
        currentColumn = 0 
        if currentRow == len(board):
            return True 
    if board[currentRow][currentColumn] == ".":
        return tryDigitsAtPosition(currentRow,currentColumn,board)
            
        
    return solvePartialSudoku(currentRow, currentColumn+1, board)


def tryDigitsAtPosition(row,column,board):
    currentRow = row
    currentColumn = column 
    for number in range(1,10):
        if isValidPosition(number,currentRow,currentColumn,board):
            board[currentRow][currentColumn] = str(number)

            if solvePartialSudoku(currentRow,currentColumn+1,board):
                return True
    board[currentRow][currentColumn] = "."
    
    return False

def isValidPosition(number,row,column,board):
    currentRow = row
    currentColumn = column
    isValidRow = str(number) not in board[row]
    isValidColumn = str(number) not in map(lambda x: x[currentColumn], board)
    
    if not isValidRow or not isValidColumn:
        return False
    
    startingRow = (row//3)*3
    startingCol = (column//3)*3
    
    for rowIndex in range(0,3):
        for columnIndex in range(0,3):
            rowToCheck = startingRow + rowIndex
            columnToCheck = startingCol + columnIndex
            if board[rowToCheck][columnToCheck] == str(number):
                return False
            
    return True