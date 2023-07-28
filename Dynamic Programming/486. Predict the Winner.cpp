class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
        int res = dfs(0, nums.size() - 1 , 1, nums);
        cout << res << '\n';
        if (res == 0) return 1;
        if (res >= 0) return res;
        return false;
    }
    int dfs(int l, int r, int t, vector<int>& nums) {
        if (l > r) return 0;
        int score = 0;
        if (t) {
            score = max(dfs(l + 1, r, 0, nums) + nums[l],dfs(l, r - 1, 0, nums) + nums[r] );
        } else {
            score = min(dfs(l + 1, r, 1, nums) - nums[l],dfs(l, r - 1, 1, nums) - nums[r] );
        }

        return score;
    }
};