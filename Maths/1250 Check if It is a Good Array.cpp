class Solution {
public:
    int euclid(int a, int b) {
        if (b == 0) return a;
        return euclid(b, a % b);
    }
    bool isGoodArray(vector<int>& nums) {
        int cur = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            cur = euclid(cur, nums[i]);
        }
        if (cur == 1) return true;

        return false;
    }
};
