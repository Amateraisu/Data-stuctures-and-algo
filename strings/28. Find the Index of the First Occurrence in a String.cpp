class Solution {
public:

vector<int> calculateZArray(const string& str) {
    int n = str.length();
    vector<int> z(n, 0);

    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
        if (i <= r) {
            z[i] = min(r - i + 1, z[i - l]);
        }
        while (i + z[i] < n && str[z[i]] == str[i + z[i]]) {
            ++z[i];
        }
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }

    return z;
}
    int strStr(string needle, string haystack) {
        int m = haystack.length();
        int n = needle.length();
        string total = haystack + "@" + needle;
        vector<int>dp = calculateZArray(total);
        int l = 0, r =0;
        for (int i = 1; i < m + n + 1; i++) {
            if (i > r) {
                l = r = i;
                while (r < m + n + 1 && total[r] == total[r - l]) {
                    r++;
                }
                dp[i] = r - l;
                r--;
            } else {
                int t = i - l;
                if (dp[t] < r - i + 1) {
                    dp[i] = dp[t];
                } else {
                    l = i;
                    while (r < m + n + 1 && total[r] == total[r - l]) {
                        r++;
                    }
                    dp[i] = r - l;
                    r--;
                }
            }
        }
        for (int i = 0; i < m + n + 1; i++) {
            if (dp[i] == haystack.length()) return i - haystack.length() - 1;
        }

        return -1;
    }
};