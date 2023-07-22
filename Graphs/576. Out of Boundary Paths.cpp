class Solution {
public:
    vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int mod = 1e9 + 7;

    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        vector<vector<vector<int>>> dp(m , vector<vector<int>>(n, vector<int>(maxMove + 1, -1)));

        return dfs(dp, startRow, startColumn, m, n, maxMove);
    }
    int dfs(vector<vector<vector<int>>>& dp, int r, int c, int m, int n, int k) {
        if (r < 0 || r >= m || c < 0 || c>=n) return 1;
        if (k == 0) return 0;
        if (dp[r][c][k] != -1) return dp[r][c][k];
        int res = 0;
        for (auto d : directions) {
            int nx = r + d[0], ny = c + d[1];
            res += dfs(dp, nx, ny , m , n, k - 1);
            res %= mod;
        }
        dp[r][c][k] = res % mod;
        return res % mod;

    }
};