class Solution {
public:
    vector<vector<pair<int, int>>>g; // {node, distance}
    int lim;
    int nodes;
    int count(int node) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>>pq;
        // use a minheap, so its
        vector<int>vis(nodes, 1e7);
        vis[node] = 0;
        pq.push({0, node});
        while (!pq.empty()) {
            auto t = pq.top();
            int cur = t.second;
            int c = t.first;
            pq.pop();
            for (auto p : g[cur]) {
                int nei = p.first, cost = p.second;
                int newCost = c + cost;
                if (newCost < vis[nei]) {
                    vis[nei] = newCost;
                    pq.push({newCost, nei});
                }

            }
        }
        int res = 0;
        for (int i =0; i < nodes ; i++) {
            if (i != node && vis[i] <= lim) res++;
            // cout << node << ' ' << i << ' ' << vis[i] << '\n';
        }
        return res;
    }
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        lim = distanceThreshold;
        nodes = n;
        g = vector<vector<pair<int, int>>>(n, vector<pair<int, int>>());

        for (auto x : edges) {
            int a = x[0], b = x[1], c = x[2];
            g[a].push_back({b, c});
            g[b].push_back({a, c});
        }
        int cur = 1e5;
        int res = -1;
        for (int i = 0; i < n; i++) {
            int r = count(i);
            if (r <= cur) {
                cur = r;
                res = i;
            }

        }
        // run dijkstra's through everything and then count the numbs.

        return res;
    }
};
