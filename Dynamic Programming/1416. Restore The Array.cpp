class Solution {
public:
    int numberOfArrays(string s, int k) {
        int n = s.length();
        vector<int> dp(n + 1, 0);
        int MOD = 1000000007;
        dp[n] = 1;

        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '0') {
                continue;
            }
            long long current = 0;
            for (int j = i; j < n ; j++) {
                current*= 10;
                current += s[j] - '0';
                if (current > k) {
                    break;
                }
                dp[i] = dp[i] % MOD + dp[j + 1] % MOD;
            }
        }


        return dp[0] % MOD;

    }
};