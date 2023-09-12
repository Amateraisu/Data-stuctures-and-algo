class Solution {
public:
    int minDeletions(string s) {
        int res = 0;
        vector<int>cnt(26, 0);
        vector<pair<int, char>>cur;
        for (auto c : s) {
            cnt[c - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            if (cnt[i] == 0) continue;
            cur.push_back(make_pair(cnt[i], i + 'a'));
        }
        sort(cur.begin(), cur.end(), [&](auto x, auto x2) {
            return x.first > x2.first;
        });
        stack<pair<int, char>>st;
        for (auto& x: cur) {
            if (!st.empty() && x.first >= st.top().first) {
                int diff = x.first - st.top().first + 1;
                if (x.first - diff <= 0) {
                    res += x.first;
                    continue;
                }
                res += diff;
                x.first -= diff;

            }
            st.push(x);
        }
        return res;
    }
};
