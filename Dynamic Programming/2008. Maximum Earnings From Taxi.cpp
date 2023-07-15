class Solution {
public:
    long long maxTaxiEarnings(int n, vector<vector<int>>& rides) {
        int m = rides.size();
        vector<long long> dp(m, -1);
        sort(rides.begin(), rides.end());

        return dfs(rides, dp, 0);
    }

    long long dfs(vector<vector<int>>& rides, vector<long long>& dp, int currentIndex) {
        if (currentIndex == rides.size()) return 0;
        if (dp[currentIndex] != -1) return dp[currentIndex];

        int next = rides.size();
        int l = currentIndex + 1, r = rides.size() - 1;

        while (l <= r) {
            int m = l + (r - l)/2;
            if (rides[currentIndex][1] <= rides[m][0]) {
                next = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }


        long long op1 = dfs(rides, dp, currentIndex + 1);
        long long op2 = rides[currentIndex][1]-rides[currentIndex][0] + rides[currentIndex][2] + dfs(rides, dp , next);
        long long best = max(op1, op2);
        dp[currentIndex] = best;
        cout << currentIndex << " " << best << endl;

        return best;
    }
};