class Solution {
public:
    vector<int>xDir = {-1, 1, 0, 0};
    vector<int>yDir = {0, 0, -1, 1};
    int m;
    int n;
    bool ok(vector<vector<int>>& heights, int mid) {

        queue<pair<int, int>>q;
        q.push(make_pair(0,0));
        vector<vector<int>>visited(m, vector<int>(n , 0));
        while (!q.empty()) {
            auto x = q.front();
            if (x.first == m - 1 && x.second == n - 1) return true;
            q.pop();
            for (int i = 0; i < 4; i++) {
                int nx = x.first + xDir[i];
                int ny = x.second + yDir[i];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && visited[nx][ny] == 0 && abs(heights[nx][ny] - heights[x.first][x.second]) <= mid) {
                    visited[nx][ny] = 1;
                    q.push(make_pair(nx, ny));

                }
            }
        }
        return false;

    }

    int minimumEffortPath(vector<vector<int>>& heights) {
        m = heights.size();
        n = heights[0].size();
        int r = 1e7;
        int l = 0;
        int res = r;
        while (l <= r) {
            int m = l + (r - l)/2;
            if (ok(heights, m)) {
                res = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }


        return res;

    }
};
