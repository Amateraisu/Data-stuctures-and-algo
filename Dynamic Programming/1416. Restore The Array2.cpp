class Solution {
    int MOD = 1e9 + 7;
public:
    int numberOfArrays(string s, int k) {
        int n = s.length();
        vector<int> dp(n + 1, 0);
        dp[n] = 1;
        for (int i = n - 1; i >= 0 ;i--) {
            long long current = 0;
            for (int j = i; j < n; j++) {
                current = current * 10 + (s[j] - '0');
                if (current == 0) break;
                if (current > k) break;
                dp[i] = dp[i] % MOD + dp[j + 1] % MOD;
            }
        }

        return dp[0] % MOD;

    }
};