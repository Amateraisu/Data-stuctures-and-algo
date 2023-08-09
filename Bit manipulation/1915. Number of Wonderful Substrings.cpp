class Solution {
public:
    long long wonderfulSubstrings(string word) {
        int mask = 0;
        unordered_map<int, int> cnt;
        cnt[0] = 1;
        long long res = 0;
        for (auto c: word) {
            int idx = c - 'a';
            mask ^= 1 << idx;
            res += cnt[mask];
            for (int i = 0; i < 10 ; i++) {
                int ne = mask ^ (1 << i);
                res += cnt[ne];
            }
            cnt[mask]++;
        }
        return res;
    }
};