class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # lets do dfs iteratively because it is the easiest to do 
        # we could also do dfs iteratively with a stack 
        # we could also do breadth first search, iteratively by using a queue   # or recursively, anyhoo 
        
        
        # time complexity would be O(m*n) where m is  the width and n is the height 
        # space complexity would be O(m*n) to store the visited data structure 
        

        res = 0 
        
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                if visited[i][j]:
                    continue
                currentIslandSize = dfs(i, j, visited, grid)
                res = max(res, currentIslandSize)

                
        return res
    
def dfs(row, column, visited, grid):

    queue = []
    res = 1
    queue.append([row, column])
    visited[row][column] = True 
    while queue:
        currentNode = queue.pop()
        currentRow, currentCol = currentNode 

        neighbours = getNeighbours(visited, currentRow, currentCol, grid)
        
        for neighbour in neighbours:
            res += 1 
            newRow, newCol = neighbour

            queue.append(neighbour)
            visited[newRow][newCol] = True
            
    return res 


def getNeighbours(visited, row, column, grid):
    neighbours = []
    if row > 0 and not visited[row - 1][column] and grid[row -1][column] == 1:
        neighbours.append([row-1, column])
    
    if row < len(grid) - 1 and not visited[row+1][column] and grid[row+ 1][column] == 1:
        neighbours.append([row+ 1, column])
    
    if column > 0 and not visited[row][column -1] and grid[row][column - 1] == 1:
        neighbours.append([row, column - 1])
    
    if column < len(grid[0]) - 1 and not visited[row][column + 1] and grid[row][column + 1] == 1:
        neighbours.append([row, column + 1])
    return neighbours