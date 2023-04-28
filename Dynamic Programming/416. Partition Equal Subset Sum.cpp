class Solution {
public:
    bool canPartition(vector<int>& nums) {
        float t = 0;
        for (int num:nums) t+= num;
        int target = t/2;
        if (t/2 != target) return false;
        int n = nums.size();
        vector<vector<bool>> dp(n + 1, vector<bool> (target + 1, false));
        // target is 11, working backwards, can we get it ?
        dp[n][target] = true;
        for (int i = n - 1; i >= 0; i--) {
            int cur = nums[i];
            for (int j = target; j >= 0 ;j--) {
                if (j + cur <= target) {
                    dp[i][j] = dp[i + 1][j] || dp[i + 1][j + cur];

                } else {
                    dp[i][j] = dp[i + 1][j];
                }

            }
        }
        for (int i = 0; i <= n;i++) {
            if (dp[i][0]) return true;
        }
        return false;


    }
};