class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int c = 0;
        int res = INT_MIN;
        for (int i = 0; i < n; i++) {
            c += nums[i];
            res = max(res, c);
            if (c < 0) {
                c = 0;
            }



        }

        return res;

    }
};