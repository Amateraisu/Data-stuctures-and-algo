class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> colors(n, 0);

        for (int i = 0; i < n; i++) {
            if (colors[i] == 0) {
                if (!dfs(i, 1, colors,graph)) return false;
            }
        }

        return true;

    }

    bool dfs(int node, int color, vector<int>& colors, vector<vector<int>>& graph) {
        if (colors[node] != 0) {
            // check if the colors match the expected color here

            if (colors[node] != color) return false;

            return true;
        }

        colors[node] = color;
        for (int i = 0; i < graph[node].size(); i++) {
            if (color == 1) {
                if (!dfs(graph[node][i], 2, colors, graph)) return false;
            } else {
                if (!dfs(graph[node][i], 1, colors, graph)) return false;
            }
        }

        return true;


    }
};