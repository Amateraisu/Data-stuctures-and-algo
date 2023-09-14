class Solution {
public:
    int n = 100;
    vector<int>vis;
    vector<vector<int>>g;
    bool dfs(int cur, int prev) {

        for (auto x : g[cur]) {
            if (vis[x] == -1) {
                int newColor = 1^prev;
                vis[x] = newColor;
                if (!dfs(x, newColor)) return false;
            } else {
                if (vis[x] == prev) return false;
            }
        }
        return true;

    }

    bool isBipartite(vector<vector<int>>& graph) {
        vis = vector(n, -1);
        g = vector<vector<int>>(n);
        for (int i = 0; i < graph.size(); i++) {
            for (int j = 0; j < graph[i].size(); j++) {
                g[i].push_back(graph[i][j]);
            }
        }

        int length = graph.size();
        for (int i = 0; i < length; i++) {
            if (vis[i] == -1) {
                vis[i] = 1;
                if (!dfs(i, 1)) return false;
            }
        }

        return true;
    }
};
