from collections import deque


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # I need to store like orientations of each island 
        # I need a way such that I can know whether my island is distinct or not 
        # what if I return the result of every single search and check if they are equals? 
        
        
        
        seen = set()
        
        
        numRows, numCols = len(grid), len(grid[0])
        visited = set()
        res = 0 
        def dfs(row, col, grid, orientations):
            

            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            queue = deque()
            queue.append((row, col, 0 , 0))
            visited.add((row, col))
            while queue:
                currentNode = queue.popleft()
                currentRow , currentCol, currentX, currentY = currentNode 
                for direction in directions:
                    newX = currentRow + direction[0]
                    newY = currentCol + direction[1]
                    if not (newX < 0 or newY < 0 or newX >= len(grid) or newY >= len(grid[0]) or grid[newX][newY] == 0 or (newX, newY) in visited):
                        visited.add((newX, newY))
                        newDirec = [currentX + direction[0], currentY + direction[1]]
                        orientations.append(currentX + direction[0])
                        orientations.append(currentY + direction[1])
                        queue.append([newX, newY, currentX + direction[0],currentY + direction[1] ])
                    
            return orientations
                    
                    
                
                
            
            
            
            
            
            
        for row in range(numRows):
            for col in range(numCols):
                if (row, col) not in visited and grid[row][col] == 1:
                    
                    result = dfs(row, col, grid, [])
                    result = tuple(result)
                    if result not in seen:
                        res += 1 
                        seen.add(result)
            
        return res
    