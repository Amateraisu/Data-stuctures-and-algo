class Solution {
public:
    vector<int>cnt;
    vector<int>res;
    int N;
    vector<vector<int>>g;
    void dfs1(int cur = 0, int p = -1) {
        cnt[cur] = 1;
        for (auto x : g[cur]) {
            if (x != p) {
                dfs1(x, cur);
                cnt[cur] += cnt[x];
                res[cur] += res[x] + cnt[x];
            }
        }
    }

    void dfs2(int cur = 0 , int p = -1) {

        for (auto x : g[cur]) {
            if (x != p) {
                res[x] = res[cur] - cnt[x] + N - cnt[x];
                dfs2(x, cur);
            }
        }
    }
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        res.resize(n);
        g.resize(n);
        cnt.resize(n);
        for (auto& x : edges) {
            int a = x[0], b = x[1];
            g[a].push_back(b);
            g[b].push_back(a);
        }

        N= n;

        dfs1();
        dfs2();

        return res;
    }
};