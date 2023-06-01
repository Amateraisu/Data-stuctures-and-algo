class Solution {
int MOD = 1e9 + 7;
public:
    int countPaths(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> cache(m, vector(n, -1));

        int res = 0;

        for (int i = 0; i < m ;i++) {
            for (int j = 0; j < n; j++) {
                res = (res % MOD + dfs(cache, grid, i, j, -1) % MOD) % MOD;

            }
        }

        return res;

    }

    int dfs(vector<vector<int>>& cache, vector<vector<int>>& grid, int row, int col, int prev) {
        if (row < 0 || row >= grid.size() || col < 0 || col >= grid[0].size() || prev >= grid[row][col]) return 0;
        if (cache[row][col] != -1) return cache[row][col];

        int best = 1;
        best = (best + dfs(cache, grid, row + 1, col, grid[row][col]) % MOD) % MOD;
        best = (best + dfs(cache, grid, row, col + 1, grid[row][col]) % MOD) % MOD;
        best = (best + dfs(cache, grid, row - 1, col, grid[row][col]) % MOD) % MOD;
        best = (best + dfs(cache, grid, row , col - 1, grid[row][col]) % MOD) % MOD;
        cache[row][col] = best;

        return best;

    }
};