class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # we can use dijkstra's algorithm 
        minTime = grid[0][0]
        numRows = numCols = len(grid[0])
        minHeap = [[grid[0][0], 0,0]]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        visited = set()
        while minHeap:
            currentValue, currentRow, currentCol = heapq.heappop(minHeap)

            minTime = max(currentValue, minTime)
            if currentRow == numRows -1 and currentCol == numCols -1:
                return minTime
            
            for direction in directions:
                newRow = currentRow + direction[0]
                newCol = currentCol + direction[1]
                if 0 <= newRow <= numRows -1 and 0 <= newCol <= numCols -1 and (newRow, newCol) not in visited:
                    
                    heapq.heappush(minHeap, [grid[newRow][newCol], newRow, newCol])
                    visited.add((newRow, newCol))
        return 0