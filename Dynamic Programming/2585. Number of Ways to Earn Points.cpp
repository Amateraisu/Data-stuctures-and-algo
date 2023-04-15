class Solution {
public:
    int waysToReachTarget(int target, vector<vector<int>>& types) {
        int n = types.size();
        vector dp(target + 1, vector<int>(n + 1)); // rows will be the score, cols will be the pile number
        int mod = 1000000007;
        // the first row will all be 1s
        for (int i = 0; i < n + 1; i++) {
            dp[0][i] = 1;
        }

        for (int i = 1; i < target + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                vector<int> pile = types[j - 1];
                for (int count = 0; count < pile[0] + 1; count++) {
                    int score = count * pile[1];
                    if (i - score >= 0) {
                        dp[i][j] = dp[i - score][j - 1] % mod + dp[i][j] % mod;
                    }
                }
            }
        }

        return dp[target][n] % mod;

    }
};