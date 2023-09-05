using ll = long long;
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        // I should first sort it
        // then afterwards keep track of the maximum element I can
        // first sort it first, then find the difference array
        sort(nums.begin(), nums.end());
        int n = nums.size();
        ll cur = 0;
        int res = 1;
        int l = 0;

        for (int i = 0; i < n ; i++) {
            cur += nums[i];
            while ((ll)nums[i] * (i - l + 1) > cur + k) {
                cur -= nums[l];
                l++;
            }
            res = max(res, i - l + 1);

        }
        return res;
    }
};