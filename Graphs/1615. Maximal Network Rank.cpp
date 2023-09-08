class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        vector<int>cnt(n, 0);
        vector<vector<int>>connected(n, vector<int>(n, 0));
        for (auto& r : roads) {
            cnt[r[0]]++;
            cnt[r[1]]++;
            connected[r[0]][r[1]] = -1, connected[r[1]][r[0]] = -1;
        }
        int res = 0;
        for (int i = 0; i < n ; i++) {
            for (int j = 0 ; j < n;j++) {
                if (i != j) {
                    res = max(res, cnt[i] + cnt[j] + connected[i][j]);
                }
            }
        }
        return res;



    }
};