class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows , num_cols = len(grid), len(grid[0])
        
        minutes = -1 
        queue = deque()
        freshOranges = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue 
                if grid[i][j] == 1:
                    freshOranges += 1 
                elif grid[i][j] == 2:
                    queue.append((i,j))
        # print(freshOranges)
        if freshOranges == 0:
            return 0 
        freshOranges += len(queue)
        while queue:
            queueLength = len(queue)
            
            for k in range(queueLength):
                row, col = queue.popleft()
                
                if row - 1 >= 0 and grid[row - 1][col] == 1: 
                    grid[row - 1][col] = 2
                    queue.append((row - 1, col))
                
                if row + 1 < len(grid) and grid[row + 1][col] == 1: 
                    grid[row + 1][col] = 2
                    queue.append((row + 1, col))
                    
                if col - 1 >= 0 and grid[row][col - 1] == 1: 
                    grid[row][col - 1] = 2
                    queue.append((row, col - 1))
                    
                if col + 1 < num_cols and grid[row][col + 1] == 1: 
                    grid[row][col + 1] = 2
                    queue.append((row, col + 1))
                freshOranges -=1
            minutes += 1 
            
        if freshOranges != 0:
            return -1 
        else:
            return minutes