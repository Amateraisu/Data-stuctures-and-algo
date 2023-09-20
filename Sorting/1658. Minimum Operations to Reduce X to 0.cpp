class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        // I cant do this greedily because it requires me to remove previous elements first 
        // 
        int n = nums.size();
        int tot = 0;
        for (int i = 0; i < n; i++) tot += nums[i];
        int g = tot - x;
        int l = 0;
        int cur = 0;
        if (g < 0) return -1;
        if (g == 0) return n;
        int res = -1;
        for (int r = 0; r < n; r++) {
            cur += nums[r];
            while (cur > g && l <= r) {
                cur -= nums[l];
                l++;
            }
            if (cur == g) {
                res = max(res, r - l + 1);
            }
        }
        if (res == -1) return -1;
        cout << res << '\n';
        return n - res;
    }
};