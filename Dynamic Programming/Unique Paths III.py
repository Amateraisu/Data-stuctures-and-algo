class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0 ), (1, 0), (0, -1), (0, 1)]
        
        
        visited = set()
        # count number of valid squares 
        
        numRows = len(grid)
        numCols = len(grid[0])
        validSquares = 0 
        starting = [0, 0]
        
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 0:
                    validSquares += 1 
                if grid[row][col] == 1:
                    starting = [row, col]

        
        visited.add((starting[0], starting[1]))
        # can improve space if we replace visited as in position instead, modifying the grid given to us 
        def dfs(row, col):

            if grid[row][col] == 2 and len(visited) - 1 == validSquares :
                # print(visited)
                return 1 
            if grid[row][col] == 2:
                return 0
                
            
            res = 0 
            visited.add((row, col))
            for direction in directions:
                newX = row + direction[0]
                newY = col + direction[1]
                if newX < 0 or newX >= numRows or newY < 0 or newY >= numCols or (newX, newY) in visited or grid[row][col] == -1:
                    continue 
                res += dfs(newX, newY)
            visited.remove((row, col))
            return res 
        
        
        return dfs(starting[0], starting[1])