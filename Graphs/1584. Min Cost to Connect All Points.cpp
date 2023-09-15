class Solution {
public:
    int find(int node, vector<int>& parents) {
        if (parents[node] != node) {
            parents[node] = find(parents[node], parents);
        }
        return parents[node];
    }
    int minCostConnectPoints(vector<vector<int>>& points) {
        int cost = 0;
        vector<vector<int>>l;
        int n = points.size();
        vector<int>parents(n, -1);
        auto u = [&](int n1, int n2) {
            int p1 = find(n1, parents);
            int p2 = find(n2, parents);
            if (p1 == p2) return 0;

            parents[p1] = p2;
            return 1;
        };
        for (int i = 0; i < n; i++) parents[i] = i;
        for (int i = 0; i < n; i++) { // get the cost, then i, j : (cost, i, j)
            for (int j = i + 1; j < n; j++) {
                if (j != i) {
                    vector<int>p1 = points[i];
                    vector<int>p2 = points[j];
                    int diff = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]);
                    l.push_back({diff, i, j});
                }
            }
        }
        sort(l.begin(), l.end());
        for (auto& x : l) {
            int f = u(x[1], x[2]);
            if (f) {
                cost += x[0];
            }
        }
        return cost;

    }
};