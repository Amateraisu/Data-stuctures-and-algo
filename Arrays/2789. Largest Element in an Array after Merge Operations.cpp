class Solution {
public:
    long long maxArrayValue(vector<int>& nums) {
        int n = nums.size();
        long long res = nums[n - 1];
        long long ret = res;
        for (int i = n - 2; i >= 0 ; i--) {
            if (nums[i] <= res) {
                res += nums[i];
            } else {
                res = nums[i];
            }
            ret = max(ret, res);
        }
        return ret;
    }
};