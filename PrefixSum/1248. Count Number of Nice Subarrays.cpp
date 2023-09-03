class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        map<int, int>mp;
        mp[0] = 1;
        int n = nums.size();
        vector<int>dp(n, 0);
        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 == 1) dp[i] = 1;
        }
        int res = 0, cnt = 0;
        for (int i = 0; i < n; i++) {
            cnt += dp[i];
            res += mp[cnt - k];
            mp[cnt]++;
        }
        return res;
    }
};