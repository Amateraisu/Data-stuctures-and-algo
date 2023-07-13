class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        vector<int> s;

        int n = graph.size();
        vector<int> dp(n, -1);
        vector<int> isVisiting(n, -1);
        for (int i = 0; i < n; i++) {
            if (dfs(i, graph, dp, isVisiting)) s.push_back(i);
        }
        return s;



    }

    int dfs(int node, vector<vector<int>>& graph, vector<int>& dp, vector<int>& isVisiting) {
        if (graph[node].size() == 0) return 1;
        if (isVisiting[node] != -1) return 0;
        if (dp[node] != -1) return dp[node];

        int can = 1;
        isVisiting[node] = 1;
        for (auto nei: graph[node]) {
            int res = dfs(nei, graph, dp, isVisiting);
            can &= res;
        }
        isVisiting[node] = -1;
        dp[node] = can;
        return can;
    }



};