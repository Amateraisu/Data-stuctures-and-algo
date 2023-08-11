class Solution {
public:
    int mod = 1e9 + 7;
    int waysToReachTarget(int target, vector<vector<int>>& types) {
        int n = types.size();
        vector<vector<int>>dp(target, vector<int>(n, -1));
        return dfs(target, types, dp, 0, 0);
    }

    int dfs(int target, vector<vector<int>>& types, vector<vector<int>>& dp, int score, int index) {
        if (score == target) return 1;
        if (index >= types.size()) return 0;
        if (dp[score][index] != -1) return dp[score][index];

        int res = 0;
        int s = types[index][1];
        for (int i = 0; i <= types[index][0] ; i++) {
            int g = s * i;
            if (score + g <= target) {
                res = (res + dfs(target, types, dp, score + g, index + 1) % mod) % mod;
            }
        }
        dp[score][index] = res % mod;

        return res % mod;
    }
};