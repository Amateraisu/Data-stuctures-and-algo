class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        queue<vector<int>> q;
        q.push({headID, 0});
        map<int, vector<int>> subs;
        int m = manager.size();
        for (int i = 0; i < m; i++) subs[manager[i]].push_back(i);
        int res = 0;
        while (!q.empty()) {
            auto front = q.front();
            q.pop();
            res = max(res, front[1]);
            int c = informTime[front[0]];
            for (int i = 0; i < subs[front[0]].size(); i++) {
                q.push({subs[front[0]][i], front[1] + c});
            }
        }
        return res;
    }
};