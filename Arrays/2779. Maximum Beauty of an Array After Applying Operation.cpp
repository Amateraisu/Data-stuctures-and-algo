class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        map<int, int> mp;
        for (int x: nums) {
            mp[x - k]++;
            mp[x + k + 1]--;
        }
        int res{0}, cur{0};
        for (auto [_, v] : mp) {
            cur += v;
            res = max(res, cur);
        }

        return res;
    }
};