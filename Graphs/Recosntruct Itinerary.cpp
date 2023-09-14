class Solution {
public:
    unordered_map<string, deque<string>>g;
    vector<string>res;
    void eulerPath(string curr) {
        while(!g[curr].empty()) {
            auto edge = g[curr].front();
            g[curr].pop_front();
            eulerPath(edge);
        }
        res.push_back(curr);
    }
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for(auto edge: tickets)
            g[edge[0]].push_back(edge[1]);
        for(auto [vertex, edges]: g)
            sort(g[vertex].begin(), g[vertex].end());
        eulerPath("JFK");
        reverse(res.begin(), res.end());
        return res;
    }
};
