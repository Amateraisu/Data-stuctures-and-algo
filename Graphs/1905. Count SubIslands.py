class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        numRows = len(grid1)
        numCols = len(grid1[0])
        mapper = {}
        res = 0 
        for row in range(numRows):
            for col in range(numCols):
                if grid1[row][col] == 1 and (row, col) not in mapper:
                    # do an island traversal 
                    visited = set()
                    self.dfs(grid1, row, col, visited)

                    for grid in visited:
                        mapper[grid] = visited 
        # then go through grid2 
        # print(mapper)
        seen = set()
        for row in range(numRows):
            for col in range(numCols):
                if grid2[row][col] == 1 and (row, col) not in seen:
                    currentSet = set()
                    self.dfs2(grid2, row, col, seen, currentSet)
                    
                    if (row, col) in mapper and currentSet.issubset(mapper[(row, col)]):
                        res += 1 
        return res
        
        
    def dfs(self, grid, row, col, seen):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return 
        seen.add((row, col))
        
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for direction in directions:
            newX = row + direction[0]
            newY = col + direction[1]
            if (newX, newY) not in seen :
                self.dfs(grid, newX, newY, seen)
                
        return 
    
    def dfs2(self, grid, row, col, seen, currentSet):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return 
        seen.add((row, col))
        currentSet.add((row, col))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for direction in directions:
            newX = row + direction[0]
            newY = col + direction[1]
            if (newX, newY) not in seen :
                self.dfs2(grid, newX, newY, seen, currentSet)
                
        return 