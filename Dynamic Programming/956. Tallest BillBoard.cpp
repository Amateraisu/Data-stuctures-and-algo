class Solution {
public:
    int tallestBillboard(vector<int>& rods) {
        int n = rods.size();
        vector<vector<int>> dp(n, vector<int>(10000, -1));

        return dfs(0, 0, dp, rods);
    }


    int dfs(int diff, int index, vector<vector<int>>& dp, vector<int>& rods) {
        if (index == rods.size()) {
            if (diff != 0) {
                return -1e9;
            }
            return 0;
        }
        if (dp[index][diff + 5000] != -1) return dp[index][diff+ 5000];

        int best = -1e9;
        int cur = rods[index];
        best = max(best, dfs(diff, index + 1, dp, rods));
        best = max(best, cur + dfs(diff + cur, index + 1, dp, rods));
        best = max(best, dfs(diff - cur, index + 1, dp , rods));
        dp[index][diff + 5000] = best;
        return best;
    }


};