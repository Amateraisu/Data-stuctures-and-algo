class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int med;
        med = static_cast<double>(nums[n/2]) + static_cast<double>(nums[(n - 1)/2]);
        med /= 2;
        if (n % 2 != 0) {
            med = nums[n/2];
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            res += abs(nums[i] - med);
        }
        return res;

    }
};
