class Solution {
public:
    long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
        int n = nums.size();
        vector<int>dp(n, 0);
        for (int i = 0; i < n ; i++) {
            if (nums[i] % modulo == k) dp[i] = 1 ,cout << '1' << '\n';
        }
        map<int, int>mp;
        mp[0]++;
        long long ret = 0, cur = 0;
        for (auto x : dp) {
            cur += x;
            cur %= modulo;
            ret += mp[(cur - k + modulo) % modulo];
            mp[cur]++;
        }
        // cout << cur << '\n';
        return ret;
    }
};