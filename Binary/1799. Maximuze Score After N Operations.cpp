class Solution {
public:
    int backtrack(vector<int>& nums, int mask, int pairsPicked, vector<int>& memo) {
        if (2 * pairsPicked == nums.size()) {
            return 0;
        }
        if (memo[mask] != -1) return memo[mask];
        int best = 0;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (((mask >> i) & 1) == 1 || ((mask >> j) & 1) == 1) continue;
                int newMask = mask | (1 << i) | 1 << j;
                int score = (pairsPicked + 1) * __gcd(nums[i], nums[j]);
                int remain = backtrack(nums, newMask, pairsPicked + 1, memo);

                best = max(best, remain + score);
            }
        }

        memo[mask] = best;
        return best;
    }
    int maxScore(vector<int>& nums) {
        int memoSize = 1 << nums.size();
        vector<int> memo(memoSize, -1);
        return backtrack(nums, 0, 0, memo);

    }
};