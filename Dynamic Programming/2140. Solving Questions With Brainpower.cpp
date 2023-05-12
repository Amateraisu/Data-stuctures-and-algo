class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        if (n == 1) {
            return questions[0][0];
        }
        vector<long long>dp (n, 0);
        dp[n - 1] = questions[n - 1][0];
        for (int i = n - 2; i >= 0; i--) {
            int nex = i + questions[i][1] + 1;
            dp[i] = questions[i][0];
            if (nex < n) dp[i] += dp[nex];
            dp[i] = max(dp[i + 1], dp[i]); // if we skip, we have dp[i + 1], if we do, we have dp[i]
        }

        return dp[0];




    }
};