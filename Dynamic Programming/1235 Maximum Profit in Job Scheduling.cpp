class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = startTime.size();
        vector<vector<int>> jobs(n, vector<int>(3, -1));
        for (int i = 0; i < n; i++) {
            jobs[i][0] = startTime[i];
            jobs[i][1] = endTime[i];
            jobs[i][2] = profit[i];
        }
        sort(jobs.begin(), jobs.end());
        vector<int> starts(n, -1);
        for (int i = 0; i < n; i++) starts[i] = jobs[i][0];
        vector<int> dp(n, -1);
        return dfs(starts, 0, jobs, dp);
    }

    int dfs(vector<int>&starts, int currentIndex, vector<vector<int>>& jobs, vector<int>& dp) {
        if (currentIndex == starts.size()) return 0;
        if (dp[currentIndex] != -1) return dp[currentIndex];

        int l = currentIndex + 1;
        int r = starts.size() - 1;
        int t = r + 1;
        while (l <= r) {
            int mid = l + (r - l)/2;
            if (starts[mid] >= jobs[currentIndex][1]) {
                t = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        int res = 0;
        res = max(res, dfs(starts, currentIndex + 1, jobs, dp));
        res = max(res, dfs(starts, t, jobs, dp) + jobs[currentIndex][2]);
        dp[currentIndex] = res;
        return res;

    }
};