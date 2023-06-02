class Solution {
    public:
    int wiggleMaxLength(vector<int> nums) {
        int n = nums.size();
        vector<int> pos(n, 1);
        vector<int> neg(n, 1);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i ; j++) {
                // if this number is smaller than j,
                if (nums[j] < nums[i]) pos[i] = max(pos[i], neg[j] + 1);
                if (nums[j] > nums[i]) neg[i] = max(neg[i], pos[j] + 1);
            }
        }
        return max(*max_element(pos.begin(), pos.end()), *max_element(neg.begin(), neg.end()));
    }
};
