class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        map<int, int>mp;
        int res{0}, l{0};
        int n = s.length();
        int c{0};
        for (int i = 0; i < n; i++) {
            char current = s[i];

            if (mp[current - 'a'] == 0) c++;
            mp[current - 'a']++;
            while (c > k) {
                mp[s[l] - 'a']--;
                if (!mp[s[l] - 'a']) c--;
                l++;
            }
            res = max(res, i - l + 1);
        }
        return res;
    }
};