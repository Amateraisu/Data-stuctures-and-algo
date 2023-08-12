class Solution {
public:
    int numberOfSubstrings(string s) {
        int res = 0;
        vector<int>count(26, 0);
        // check indexes 0, 1, 2 such that they are at least 1
        int l = 0;
        int n = s.length();
        for (int r = 0; r < n; r++) {
            char c = s[r];
            count[c - 'a']++;
            while (count[0] > 0 && count[1] > 0 && count[2] > 0) {
                count[s[l] - 'a']--;
                l++;
            }
            res += l;
        }

        return res;

    }
};