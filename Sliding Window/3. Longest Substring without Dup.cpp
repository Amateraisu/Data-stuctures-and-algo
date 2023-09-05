class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int>mp;
        int r = -1;
        int n = s.length();
        int res = 0;
        for (int l = 0; l < n; l++) {
            while (r < n - 1 && (mp[s[r + 1]] == 0)) {
                r++;
                mp[s[r]]++;

            }
            res = max(res, r - l + 1);
            mp[s[l]]--;

        }

        return res;
    }
};