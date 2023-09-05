class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        deque<pair<int, int>>q;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if (!q.empty() && q.front().second < i - k + 1) {
                q.pop_front();
            }
            while (!q.empty() && q.back().first < nums[i]) {
                q.pop_back();
            }
            q.push_back({nums[i], i});
            if (i - k + 1 >= 0) res.push_back(q.front().first);
        }

        return res;
    }
};