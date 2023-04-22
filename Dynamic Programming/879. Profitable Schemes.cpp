class Solution {
public:
    int mod = 1e9 + 7;
    int dp[101][101][101];
    int profitableSchemes(int n, int minProfit, vector<int>& group, vector<int>& profits) {
        for (int count = 0; count <= n; count++) {
            dp[group.size()][count][minProfit] = 1; // count is the number of members used so far, so by default not caring about the number of members we use, with the whole case, we know that it will be 1
        }
        for (int index = group.size() - 1; index >=0; index--) {
            for (int count = 0; count <=n; count++) {
                for (int profit = 0; profit <= minProfit; profit++) {
                    dp[index][count][profit] = dp[index + 1][count][profit];
                    if (count + group[index] <= n) {
                        dp[index][count][profit] = (dp[index][count][profit] + dp[index + 1][count + group[index]][min(minProfit, profit + profits[index])]) % mod;
                    }
                }
            }
        }

        return dp[0][0][0];



    }
};