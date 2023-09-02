class Solution {
public:
string s;
vector<string>w;
vector<string>r;
    void dfs(int currentIndex, vector<string>& cur) {
        if (currentIndex == s.length()) {
            string res = "";
            for (auto& c : cur) {
                res += c + " ";
            }
            // cout << "END " << res << '\n';
            res = res.substr(0, res.length() - 1);
            r.push_back(res);
            return;
        }
        for (auto& word: w) {
            int length = word.length();
            if (currentIndex + length <= s.length() && s.substr(currentIndex, length) == word) {
                cur.push_back(word);
                dfs(currentIndex + length, cur);
                cur.pop_back();
            }

        }
        return ;
    }
    vector<string> wordBreak(string str, vector<string>& wordDict) {
        // we have to use backtracking here
        s = str;
        w = wordDict;
        vector<string>t;
        dfs(0, t);

        // for (auto& word : r) {
        //     cout << word << '\n';
        // }

        return r;
    }
};