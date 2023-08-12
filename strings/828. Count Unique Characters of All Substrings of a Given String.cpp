class Solution {
public:
int mod = 1e9 + 7;
    int uniqueLetterString(string s) {
        unordered_map<int, vector<int>> mp;
        for (int i = 0; i < 26; i++) {
            mp[i].push_back(-1);
        }
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            mp[c - 'A'].push_back(i);
        }
        int res = 0, n = s.length();
        for (int i = 0; i < 26; i++) {
            mp[i].push_back(n);
        }
        for (int i = 0; i < 26; i++) {
            for (int j = 1; j < mp[i].size() - 1; j++) {
                int l = mp[i][j] - mp[i][j - 1], r = mp[i][j + 1] - mp[i][j];
                res += l * r;
            }
        }

        return res;
    }
};