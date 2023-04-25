class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        int c = 0;
        for (int i = 0; i < n ; i++) {
            if (nums[i] == 1) {
                c++;
            }
        }
        if (c == 0) {
            return 1;
        }
        for (int i = 0; i < n ; i++) {
            if (nums[i] <= 0) {
                nums[i] = 1;
            }
        }
        for (int i = 0; i < n ; i++) {
            if (nums[i] <= n && nums[abs(nums[i]) - 1] > 0) {
                nums[abs(nums[i]) - 1] *= -1;
            }
        }
        for (int i =0; i < n; i++) {
            if (nums[i] > 0) {
                return i + 1;
            }
        }

        return n + 1;



    }
};