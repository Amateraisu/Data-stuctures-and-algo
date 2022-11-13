class Solution:
    def minArea(self, grid: List[List[str]], x: int, y: int) -> int:
        # just find the area of the black pixels, get the height and width 
        # find width 
        
        
        # --> do a depth first search in 4 directions 
        # --> can use binary search to find the boundaries also 
        
        up = x
        down = x 
        left = y 
        right = y 
        seen = set()
        def dfs(currentRow, currentCol):
            nonlocal up, down , left, right

            if currentRow < 0 or currentRow > len(grid) - 1 or currentCol < 0 or currentCol > len(grid[0]) - 1 or (currentRow ,currentCol) in seen:
                return 

            if grid[currentRow][currentCol] != "1":
                return 

            seen.add((currentRow, currentCol))
            # print(currentRow, currentCol)
            left = min(left, currentCol)
            right = max(right, currentCol)
            up = min(up, currentRow)
            down = max(down, currentRow)
            dfs(currentRow - 1, currentCol)
            dfs(currentRow + 1, currentCol)
            dfs(currentRow, currentCol - 1)
            dfs(currentRow, currentCol + 1)
            
        dfs(x, y)
        
        height = down - up + 1 
        width = right - left + 1 
        return height * width 