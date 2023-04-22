class Solution {
public:
    int findGCD(vector<int>& nums) {
        int n = nums.size();
        int maximum = INT_MIN;
        int minimum = INT_MAX;
        for (int i = 0; i < n ;i++) {
            maximum = max(maximum, nums[i]);
            minimum = min(minimum, nums[i]);
        }

        while (maximum > 0 && minimum > 0) {
            if (maximum > minimum) {
                maximum = maximum % minimum;
            } else {
                minimum = minimum % maximum;
            }


        }
        if (maximum == 0) {
            return minimum;
        }

        return maximum;

    }
};