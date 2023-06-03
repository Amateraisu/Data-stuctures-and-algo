class Solution {
public:
    int numDecodings(string s) {
        int n = s.length();
        vector<int> dp(n, -1);

        return dfs(0, s, dp);

    }

    int dfs(int index, string s, vector<int>& dp) {
        if (index > s.length()) return 0;
        if (s[index] == '0') return 0;
        if (index == s.length()) return 1;

        if (dp[index] != -1) return dp[index];
        int best = dfs(index + 1, s, dp);
        // check if 2 chars are valid
        if (index <= s.length() - 2 && stoi(s.substr(index, 2)) <= 26) best += dfs(index + 2, s, dp);


        dp[index] = best;
        return best;

    }
};