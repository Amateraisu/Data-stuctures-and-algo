class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        # bottom up iterative
        # O(mn^2)
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf') for i in range(n)] for j in range(m)]
        print(dp)
        for i in range(n):
            dp[-1][i] = grid[-1][i]
        for i in range(m - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                for k in range(n - 1, -1, -1):

                    dp[i][j] = min(dp[i][j], dp[i + 1][k] + grid[i][j] + moveCost[grid[i][j]][k])


        return min(dp[0])




        # for every row
        # for every col, go through all the cols under cols again
        # O(mn^2)
        # top down iterative
        #
        # m = len(grid)
        # n = len(grid[0])
        # dp = [[float('inf') for i in range(n)] for j in range(m)]
        # for i in range(n):
        #     dp[0][i] = grid[0][i]
        # for i in range(m - 1): # for every row and column, update the values underneath
        #     for j in range(n):
        #         for k in range(n):
        #             dp[i + 1][k] = min(dp[i + 1][k], grid[i + 1][k] + dp[i][j] + moveCost[grid[i][j]][k])

        # return min(dp[-1])