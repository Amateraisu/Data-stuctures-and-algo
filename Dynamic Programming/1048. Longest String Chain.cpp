class Solution {
public:
    int longestStrChain(vector<string>& words) {
        int res = 1;
        auto valid = [&](string w1, string w2) {
            int m = w1.size();
            int n = w2.size();
            if (n - m != 1) return false;
            int d = 0;
            int j = 0;
            for (int i = 0; i < n; i++) {
                if (j < m && w2[i] != w1[j]) {
                    d++;
                    continue;
                }
                j++;
            }
            return d <= 1;
        };

        auto c = [&](string w1, string w2) {
            return w1.size() < w2.size();
        };
        sort(words.begin(), words.end(), c);
        int n = words.size();
        for (int i = 0; i < n; i++) {
            cout << words[i] << '\n';
        }
        vector<int>dp(n + 1, 1);
        for (int i = 1; i < n ; i++) {
            for (int j = 0; j < i;  j++) {
                // cout << words[i] << ' ' << words[j] << '\n';
                if (valid(words[j], words[i])) {
                    // cout << "VALUID \n";
                    dp[i] = max(dp[i], dp[j] + 1);
                    res = max(res, dp[i]);
                }
            }
        }

        return res;

    }
};
