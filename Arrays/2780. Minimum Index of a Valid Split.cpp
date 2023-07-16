class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        unordered_map<int, int> mp;
        for (int x : nums) mp[x]++;
        pair<int, int> mx;
        for (auto [k, v]: mp) mx = max(mx, {v, k});
        int n = nums.size();
        int use = mx.second;
        vector<int> ps(n, -1);
        int c = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == use) c += 1 ;
            ps[i] = c;
        }

        for (int i = 0; i < n; i++) {

            if (ps[i] * 2 > i + 1 && (ps[n - 1] - ps[i]) * 2 > (n - i - 1)) return i;
        }
        return -1;
    }
};