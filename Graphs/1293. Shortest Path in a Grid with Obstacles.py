from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = deque()
        q.append([0, 0, k, 0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        visited.add((0, 0))
        n = len(grid)
        m = len(grid[0])
        while q:
            currentNode = q.popleft()
            row, col, remaining, cost = currentNode
            if (row, col) == (n - 1, m - 1):
                return cost
            for direction in directions:
                newX = row + direction[0]
                newY = col + direction[1]
                newK = remaining
                newCost = cost + 1
                if newX >= 0 and newX <= n - 1 and newY >= 0 and newY <= m - 1 and grid[newX][newY] == 1:
                    newK = newK - 1
                if newX >= 0 and newX <= n - 1 and newY >= 0 and newY <= m - 1 and (newX, newY, newK) not in visited and newK >= 0:
                    q.append([newX, newY, newK, newCost])
                    visited.add((newX, newY, newK))

        return -1
