class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<vector<int>> edges;
        for (int i = 0; i < buildings.size(); i++) {
            edges.push_back({buildings[i][0], i});
            edges.push_back({buildings[i][1], i});

        }

        sort(edges.begin(), edges.end());
        priority_queue<pair<int, int>> live;
        // the first key is height, second is the right edge of all buildings
        vector<vector<int>> res;
        int idx = 0;

        while (idx < edges.size()) {
            int currX = edges[idx][0];
            while (idx < edges.size() && edges[idx][0] == currX) {
                int b = edges[idx][1];

                if (buildings[b][0] == currX) {
                    int right = buildings[b][1];
                    int h = buildings[b][2];
                    live.push({h, right});
                }
                idx+=1;

            }
            while (!live.empty() && live.top().second <= currX) {
                live.pop();
            }
            int currHeight = live.empty() ? 0: live.top().first;

            if (res.empty() || res[res.size() - 1][1] != currHeight) {
                res.push_back({currX, currHeight});
            }


        }
        return res;
    }
};