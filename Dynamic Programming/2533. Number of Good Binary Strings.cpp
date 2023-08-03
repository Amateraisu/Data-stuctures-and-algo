class Solution {
public:
    int mod = 1e9 + 7;
    int goodBinaryStrings(int minLength, int maxLength, int oneGroup, int zeroGroup) {
        vector<int> dp0(maxLength + 1, 0);
        vector<int> dp1(maxLength + 1, 0);
        dp0[zeroGroup] = 1;
        dp1[oneGroup] = 1;
        for (int i = 0; i < maxLength + 1; i++) {
            if (i - zeroGroup >= 0) {
                dp0[i] += dp0[i - zeroGroup];
                dp0[i] %=  mod;
                dp0[i] += dp1[i - zeroGroup];
                dp0[i] %=  mod;
            }
            if (i - oneGroup>= 0) {
                dp1[i] += dp0[i - oneGroup] % mod;
                dp1[i] %=  mod;
                dp1[i] += dp1[i - oneGroup] % mod;
                dp1[i] %=  mod;
            }
        }
        int res = 0;
        for (int i = minLength; i < maxLength + 1; i++) {
            res += dp0[i];
            res %=  mod;
            res += dp1[i];
            res %=  mod;
        }
        return res % mod;
    }
};