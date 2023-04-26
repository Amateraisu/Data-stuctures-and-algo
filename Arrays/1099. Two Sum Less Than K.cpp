class Solution {
public:
    int twoSumLessThanK(vector<int>& nums, int k) {
        int res = INT_MIN;
        int n = nums.size();

        int l = 0;
        int r = n - 1;
        sort(nums.begin(), nums.end());

        while (l < r) {
            int total = nums[l] + nums[r];
            if (total < k) {
                res = max(res, total);
                l++;
            } else {
                r--;
            }

        }

        if (res == INT_MIN) {
            return -1;
        }

        return res;

    }
};