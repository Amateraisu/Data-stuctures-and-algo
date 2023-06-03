class Solution {
public:
    int numDecodings(string s) {
        int n = s.length();
        vector<int> dp(n + 1, 0);
        dp[n] = 1;
        for (int i = n - 1; i >= 0 ; i--) {
            if (s[i] == '0') continue;
            dp[i] += dp[i + 1];
            if (i <= n - 2 && stoi(s.substr(i, 2)) <= 26) dp[i] += dp[i + 2];
        }
        return dp[0];
    }
};