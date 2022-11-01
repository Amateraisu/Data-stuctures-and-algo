class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        numRows = len(grid)
        numCols = len(grid[0])
        res = [-1] * numCols
        
        



        for ball in range(numCols):
            can, position = canReach(ball, grid)
            # print("res", can, position, ball)
            if can:
                res[ball] = position
                
                
        return res 
    
def canReach(startCol, grid):
    currentRow, currentCol = 0, startCol
    while currentRow >= 0 and currentRow <= len(grid) - 1 and currentCol >= 0 and currentCol <= len(grid[0]) - 1:
        # need to check if the column after this 
        # current direction 
        # print(currentRow, currentCol)
        if grid[currentRow][currentCol] == 1:
            # check right side 
            if currentCol == len(grid[0]) - 1:
                return False , -1
            elif grid[currentRow][currentCol + 1] != 1:
                return False , -1
        
        if grid[currentRow][currentCol] == -1:
            # check left side
            if currentCol == 0:
                return False , -1
            elif grid[currentRow][currentCol - 1] != -1:
                return False , -1

        currentCol += grid[currentRow][currentCol]
        currentRow += 1 
        
    # print(currentCol, "startCol", startCol)
    
    return currentRow == len(grid), currentCol