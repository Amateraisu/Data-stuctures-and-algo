class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {

        // O(nk)
        // actually all we need to do is to just keep track of the top 2 elements of each row
        // to make it into O(nk)


        // O(nk^2)
        int n = costs.size();
        int k = costs[0].size();
        vector<vector<int>> dp(n, vector<int>(k, 1000000));

        for (int i = 0; i < k; i++) dp[0][i] = costs[0][i];
        for (int i = 1 ; i < n ; i++) {
            for (int j = 0; j < k ; j++) {
                for (int x = 0; x < k ; x++) { // iterate through the previous row
                    if (x != j) dp[i][j] = min(dp[i - 1][x] +costs[i][j], dp[i][j]);
                }
            }
        }
        return *min_element(dp[n-1].begin(), dp[n - 1].end());

    }
};