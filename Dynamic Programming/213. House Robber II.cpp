class Solution {
public:
    int rob1(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 0);
        if (n == 1) return nums[0];
        if (n == 2) {
            return *max_element(nums.begin(), nums.end());
        }
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);

        for (int i = 2; i < n ; i++) {
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]);
        }

        return *max_element(dp.begin(), dp.end());
    }


    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int> nums1(n - 1 , 0);
        vector<int> nums2(n - 1, 0);
        if (n == 1) return nums[0];
        if (n == 2) {
            return max(nums[0], nums[1]);
        }
        for (int i = 0; i < n - 1; i++) {
            nums1[i] = nums[i];
        }
        for (int i = 1; i < n; i++) {
            nums2[i - 1] = nums[i];
        }
        int res1 = rob1(nums1);
        int res2 = rob1(nums2);
        return max(res1, res2);
    }
};