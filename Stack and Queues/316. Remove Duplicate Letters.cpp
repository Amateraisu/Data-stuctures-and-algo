class Solution {
public:
    string removeDuplicateLetters(string s) {
        vector<int>cnt(26, 0);
        for (auto c : s) cnt[c-'a']++;
        string res = "";
        stack<string>st;
        vector<int>seen(26, 0);
        for (auto c: s) {
            cnt[c - 'a']--;
            if (seen[c - 'a']> 0) continue;
            while (!res.empty() && res.back() > c && cnt[res.back() - 'a'] > 0) {
                auto t = res.back();
                res.pop_back();
                seen[t - 'a'] = 0;
            }
            res.push_back(c);
            seen[c - 'a']++;
        }

        return res;
    }
};