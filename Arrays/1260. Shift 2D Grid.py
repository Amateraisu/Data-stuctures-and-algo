class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        new_grid = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        numberOfRows = len(grid)
        numberOfColumns = len(grid[0])
        for row in range(numberOfRows):
            for col in range(numberOfColumns):
                numberToBeMoved = grid[row][col]
                newCol = (col + k) % numberOfColumns
                # newRow = (row + (k % numberOfColumns)) % numberOfRows
                # for every 3 shifts, there is an increase in row 
                # shiftsInRow = k % numberOfColumns
                # if shif
                shiftsInRow = (col + k) // numberOfColumns
                newRow = (row + shiftsInRow) % numberOfRows
                
                new_grid[newRow][newCol] = numberToBeMoved
        return new_grid