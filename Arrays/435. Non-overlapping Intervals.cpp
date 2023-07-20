class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int prev = -1e9;
        int res = 0;
        for (const auto& interval: intervals) {
            int a = interval[0], b = interval[1];
            if (a < prev) {
                res++, prev = min(prev, b);
            } else {
                prev = max(prev, b);
            }

        }

        return res;
    }
};