class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # take the maximum path of every single grid
        # always take the maximum value in that heap
        # update the result( which is the minimum value of that path )
        # time complexity of O(mnlogmn)
        maxHeap = [(-grid[0][0], 0, 0)]
        n = len(grid)
        m = len(grid[0])
        res = float("inf")
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        while maxHeap:
            currentNode, row, col = heapq.heappop(maxHeap)
            value = currentNode * -1
            res = min(res, value)
            visited.add((row, col))
            if (row, col) == (n - 1, m - 1):
                return res
            for direction in directions:
                newX = row + direction[0]
                newY = col + direction[1]
                if newX >= 0 and newX <= n - 1 and newY >= 0 and newY <= m - 1 and (newX, newY) not in visited:

                    heapq.heappush(
                        maxHeap, (-1 * grid[newX][newY], newX, newY))

        return 0
