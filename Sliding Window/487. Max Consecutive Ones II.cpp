class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        // if I can flip at most one 1,
        int prev = -1;
        int res = 0;
        int n = nums.size();
        int c = 0;
        int l = 0;
        // we can use a sliding window here
        for (int i = 0; i < n ; i++) {
            if (nums[i] == 0) c -= 1;
            while (c < -1) {
                if (nums[l] == 0) c += 1;
                l++;
            }
            res = max(res, i - l + 1);
        }

        return res;

    }
};