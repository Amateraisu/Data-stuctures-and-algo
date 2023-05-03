class Solution {
public:
    int minPathCost(vector<vector<int>>& grid, vector<vector<int>>& moveCost) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 1'000'000'000));

        for (int i = 0; i < n ; i++) dp[m - 1][i] = grid[m - 1][i];

        for (int i = m - 2; i>= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                for (int k = n - 1; k >=0 ;k--) {
                    dp[i][j] = min(dp[i][j], dp[i + 1][k] + grid[i][j] + moveCost[grid[i][j]][k]);
                }
            }
        }

        return *min_element(dp[0].begin(), dp[0].end());
    }
};