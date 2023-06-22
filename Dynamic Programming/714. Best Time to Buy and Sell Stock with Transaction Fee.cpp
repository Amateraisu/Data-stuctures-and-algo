class Solution {

public:
    int maxProfit(vector<int>& prices, int fee) {
        int n = prices.size();
        vector<vector<int>> dp(n, vector<int> (2, -1));



        return dfs(prices, fee, dp, 0, 0);
    }
    int dfs(vector<int>& prices, int fee, vector<vector<int>>& dp, int i, int isHolding) {
        if (i == prices.size()) return 0;

        if (dp[i][isHolding] != -1) return dp[i][isHolding];
        int res = 0;

        res = max(dfs(prices, fee, dp, i + 1, isHolding), res);
        if (isHolding) {
            res = max(res, prices[i] + dfs(prices, fee, dp, i + 1, 0) - fee);

        } else {
            res = max(res, dfs(prices, fee, dp, i + 1, 1) - prices[i]);
        }

        dp[i][isHolding] = res;
        return res;
    }
};