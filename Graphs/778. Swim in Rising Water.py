class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [[grid[0][0], 0, 0]] # [cost, row , column]
        lengthOfGrid = len(grid)
        res = 0
        visited = set()
        while minHeap:
            currentCost, currentRow, currentCol = heapq.heappop(minHeap)
            if [currentRow, currentCol] == [lengthOfGrid - 1, lengthOfGrid-1]:
                res = currentCost 
                break 
            neighbours = self.getNeighbours(visited, grid, currentRow, currentCol)
            for neighbour in neighbours:
                heapq.heappush(minHeap, [max(currentCost, neighbour[0]), neighbour[1], neighbour[2]])
                
            
            
        return res
    
    
    def getNeighbours(self, visited, grid, currentRow, currentCol):
        neighbours = []
        # top 
        if currentRow - 1 >= 0 and (currentRow - 1, currentCol) not in visited:
            neighbours.append([grid[currentRow - 1][currentCol], currentRow - 1, currentCol])
            visited.add((currentRow - 1, currentCol))
            
        # bottom 
        if currentRow + 1 <= len(grid) - 1 and (currentRow + 1, currentCol) not in visited:
            neighbours.append([grid[currentRow + 1][currentCol], currentRow + 1, currentCol])
            visited.add((currentRow + 1, currentCol))
        
        # left 
        
        if currentCol - 1 >= 0 and (currentRow , currentCol - 1) not in visited:
            neighbours.append([grid[currentRow][currentCol - 1],currentRow, currentCol - 1])
            visited.add((currentRow, currentCol - 1))
        if currentCol + 1 <= len(grid) - 1 and (currentRow , currentCol + 1) not in visited:
            neighbours.append([grid[currentRow][currentCol + 1], currentRow, currentCol + 1])
            visited.add((currentRow, currentCol + 1))
        return neighbours