class Solution {
public:
    double knightProbability(int n, int k, int row, int column) {
        // row, column, number of moves left
        vector<vector<vector<double>>> dp(n, vector<vector<double>>(n, vector<double>(k + 1, -1)));


        return dfs(dp, row, column, n, k);

    }

    double dfs(vector<vector<vector<double>>>& dp, int r, int c, int n, int k) {
        // if out of the board
        if (r < 0 || r >= n || c < 0 || c >= n) return 0;
        if (k == 0) return 1;
        if (dp[r][c][k] != -1) return dp[r][c][k];
        vector<vector<int>> directions{{-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}, {1, -2}, {2, -1}, {2, 1}, {1, 2}};
        double res = 0;
        for (auto& x : directions) {
            int nx = r + x[0], ny = c + x[1];
            res += dfs(dp, nx, ny, n, k - 1);
        }

        dp[r][c][k] = res/8;
        return res/8;
    }
};