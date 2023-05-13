class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        int MOD = 1e9 + 7;
        vector<int> dp(high + 1, 0);
        dp[0] = 1;
        for (int i = 0; i < high + 1 ;i++) {
            int nextZero = i + zero;
            int nextOne = i + one;
            if (nextZero <= high) dp[nextZero] = dp[i] % MOD + dp[nextZero] % MOD;
            if (nextOne <=  high) dp[nextOne] = dp[i] % MOD + dp[nextOne] % MOD;
        }

        int res = 0;
        for (int i = low; i <= high; i++) {
            res = res % MOD + dp[i] % MOD ;
        }

        return res % MOD ;

    }
};