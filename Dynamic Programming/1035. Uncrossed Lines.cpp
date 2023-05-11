class Solution {
    vector<vector<int>> dp;
public:
    int dfs(vector<int>& nums1, vector<int>& nums2, int i1, int i2) {
        if (i1 == nums1.size() || i2 == nums2.size()) return 0;
        // if ()
        if (dp[i1][i2] != -1) return dp[i1][i2];

        int best = 0;
        if (nums1[i1] == nums2[i2]) {
            best = max(best, dfs(nums1, nums2, i1 + 1, i2 + 1) + 1);
        } else {
            best = max(best, dfs(nums1, nums2, i1 + 1, i2));
            best = max(best, dfs(nums1, nums2, i1, i2 + 1));
        }

        dp[i1][i2] = best;
        return best;
    }
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        // when drawing a line, we should always connect to the one which occupies the least width
        // once we connect the numbers, we can no longer use any number prior to them.
        int m = nums1.size();
        int n = nums2.size();
        dp.resize(m, vector<int>(n, -1));

        return dfs(nums1, nums2, 0, 0);


    }


};