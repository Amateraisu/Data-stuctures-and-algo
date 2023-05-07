class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        vector<int> dp;
        int n = obstacles.size();
        vector<int> res;
        for (int len: obstacles) {
            // binary search to find the right most index to inser this number

            if (dp.size() == 0) {
                dp.push_back(len);
                res.push_back(1);
            } else {
                int m = dp.size();
                int l = 0;
                int r = m - 1;
                int res1 = -1;
                while (l <= r) {
                    int m = l + (r - l)/2 ;
                    if (dp[m] <= len) { // valid index
                        l = m + 1;
                        res1 = m;
                    } else {
                        r = m - 1;
                    }

                }
                res1++;
                // cout << res1 << " " << len << "\n";
                if (res1 == dp.size()) {
                    dp.push_back(len);
                } else {
                    dp[res1] = len;
                }
                res.push_back(res1 + 1);

            }

        }

        return res;

    }
};