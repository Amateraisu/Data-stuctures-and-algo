class Solution {
public:
    bool winnerSquareGame(int n) {
        vector<int> dp(n + 1, 0);
        dp[0] = 0;
        vector<int> nums;
        for (int i = 1; i < int(sqrt(n)) + 1; i++) {
            if (i * i <= n) nums.push_back(i);
        }
        // for (auto num : nums) {
        //     cout << num << "\n";
        // }

        for (int i = 1; i < n + 1; i++) {
            for (int num : nums) {
                if (num * num > i) break;
                if (dp[i - num * num] == 0) dp[i] = 1;

            }
        }
        return dp[n];

    }
};