#include <algorithm>
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length();
        int n = word2.length();

        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 1; i <= n; ++i) {
            dp[0][i] = 1 + dp[0][i - 1];
        }

        word1 = " " + word1;
        word2 = " " + word2;

        for (int j = 1; j <= m; ++j) {
            dp[j][0] = 1 + dp[j - 1][0];
        }

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (word1[i] == word2[j]) {
                    dp[i][j] = min({
                        dp[i - 1][j - 1],
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1
                    });
                } else {
                    dp[i][j] = min({
                        dp[i - 1][j - 1],
                        dp[i - 1][j],
                        dp[i][j - 1]
                    }) + 1;
                }
            }
        }


        return dp[m][n];
    }
};