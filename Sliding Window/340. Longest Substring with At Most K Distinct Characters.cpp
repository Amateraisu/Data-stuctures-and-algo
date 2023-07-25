class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        unordered_map<char, int>mp;
        int c = 0;
        int n = s.length();
        int l = 0;
        int res = 0;
        for (int i = 0; i < n; i++) {
            char cs= s[i];
            mp[cs]++;
            if (mp[cs] == 1) c++;
            while (c > k) {
                mp[s[l]]--;
                if (!mp[s[l]]) {
                    c--;
                }
                l++;
            }
            res = max(res, i - l + 1);
        }
        return res;

    }
};