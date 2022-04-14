class Solution:
    def totalNQueens(self, n: int) -> int:
        columnPlacements = [0 for num in range(n)]
        
        return getNumberOfNonAttackingQueens(columnPlacements, 0, n)
    
    
    
def getNumberOfNonAttackingQueens(columnPlacements,row, boardSize):
    if row == boardSize:
        return 1
    
    validPlacements = 0 
    for column in range(boardSize):
        if isNonAttacking(columnPlacements, row, column, boardSize):
            columnPlacements[row] = column
            validPlacements += getNumberOfNonAttackingQueens(columnPlacements, row+1, boardSize)
            
    return validPlacements


def isNonAttacking(columnPlacement, row, column, boardSize):
    currentRow = row
    currentColumn = column 
    for previousColumnIndex in range(currentRow):
        previousColumn = columnPlacement[previousColumnIndex]
        
        
        sameColumn = previousColumn == currentColumn
        # it is in the same diagonal if difference between row and column is the same 
        sameDiagonal = abs(currentColumn - previousColumn) == row - previousColumnIndex
        
        if sameColumn or sameDiagonal:
            return False
        
    return True