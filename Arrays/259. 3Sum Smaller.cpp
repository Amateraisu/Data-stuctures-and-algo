class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());

        int res = 0;
        int n = nums.size();
        for (int i = 0; i < n;i++) {
            int l = i + 1;
            int r = n - 1;

            while (l < r) {
                int total = nums[i] + nums[l] + nums[r];
                if (total < target) {
                    res += r - l;
                    l++;
                } else {
                    r--;
                }
            }
        }
        return res;

    }
};