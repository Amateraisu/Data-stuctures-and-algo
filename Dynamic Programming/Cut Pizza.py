class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10 ** 9 + 7
        m = len(pizza)
        n = len(pizza[0])
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        c = 0
        # constructing the dp
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1] - dp[i + 1][j + 1]
                if pizza[i][j] == 'A':
                    dp[i][j] += 1
                c = max(c, dp[i][j])
        if not c:
            return 0

        @cache
        def dfs(row, col, cut):
            if cut == k - 1:
                return 1

            best = 0
            # if both sides have pizza, and total - remaining > 0
            for r in range(row + 1, m):
                if dp[row][col] - dp[r][col] > 0 and dp[r][col] > 0:
                    print('cut row', row, col, r)
                    best += dfs(r, col, cut + 1)
            for c in range(col + 1, n):
                if dp[row][col] - dp[row][c] > 0 and dp[row][c] > 0:
                    print('cut col', row, col, c)
                    best += dfs(row, c, cut + 1)
            return best % mod

        return dfs(0, 0, 0)