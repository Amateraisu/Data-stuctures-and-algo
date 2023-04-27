class Solution {
public:
    string minWindow(string s1, string s2) {
        int m = s1.size();
        int n = s2.size();

        vector<vector<int>> dp(m + 1, vector<int> (n + 1, 1000000000));


        dp[0][0] = 0;
        for (int i = 0; i <= m ; i++) {
            dp[i][0] = 0;
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1[i- 1] == s2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = dp[i - 1][j] + 1;
                }
            }
        }


        int endPos = -1;
        int res = m + 1;

        for (int i = 0; i <= m; i++) {
            if (dp[i][n] < res) {
                endPos = i;
                res = dp[i][n];
            }
        }
        if (endPos == -1) {
            return "";
        }



        return s1.substr(endPos - res, res);


    }
};