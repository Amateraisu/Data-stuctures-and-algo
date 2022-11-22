from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # so what if I just did a bfs on every single grid ? 
        
        # calculate the total distance required for this grid  
        # and return the minimal I got. 
        # time complexity would be O(MN)^2 
        # ~ 250 ^ 2 = 4250ms 
        
        # count hte number of buildings first 
        res = float("inf")
        numberOfBuildings = self.countBuildings(grid)
        invalids = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i, j) not in invalids:
                    
                    cost = self.countCost(i, j, grid, numberOfBuildings, invalids)
                    res = min(cost, res)


        return res if res != float("inf") else -1
        
        
    def countBuildings(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1 
                    
        return count 
    
    
    def countCost(self, row , column, grid, total, invalids):
        buildings = 0 
        queue = deque()
        queue.append([[row, column], 0])
        totalCost = 0 
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited.add((row, column))
        while queue:
            currentNode, cost = queue.popleft()
            currentRow, currentCol = currentNode
            
            
            
            if grid[currentRow][currentCol] == 1:
                # print(currentRow, currentCol, cost, "reached")
                buildings += 1 
                totalCost += cost 
                if buildings == total:
                    break 
                continue 
                    
            for direction in directions:
                newX = currentRow + direction[0]
                newY = currentCol + direction[1]
                if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[0]) or (newX, newY) in visited or grid[newX][newY] == 2:
                    continue 
                visited.add((newX, newY))
                queue.append([[newX, newY], cost + 1])
        if buildings != total:
            invalids.add((row, column))
            
        return totalCost if buildings == total else float("inf")