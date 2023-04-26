class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 0) {
            return 0;
        }
        int res = 0;
        int l = 0;
        long long cur = 1;
        int n = nums.size();
        for (int r = 0; r < n; r++) {
            cur *= nums[r];


            while (l <= r && cur >= k) {
                cur /= nums[l];
                l++;
            }
            res += r - l + 1;



        }

        return res;



    }
};