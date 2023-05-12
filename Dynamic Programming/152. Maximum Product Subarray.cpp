class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        vector<int> pos(n, -1);
        vector<int> neg(n, 1);

        pos[0] = nums[0];
        neg[0] = nums[0];
        for (int i = 1; i < n; i++) {
            vector<int> temp = {nums[i], nums[i] * pos[i - 1], nums[i] * neg[i - 1]};
            pos[i] = *max_element(temp.begin(), temp.end());
            neg[i] = *min_element(temp.begin(), temp.end());
        }

        return *max_element(pos.begin(), pos.end());
    }
};