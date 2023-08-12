class Solution {
public:
vector<int>rowDir = {0, 0, -1, 1};
vector<int>colDir = {1, -1, 0, 0};
int isValid(vector<vector<int>>& heights, int& limit) {
    queue<pair<int,int>>q;
    q.push({0, 0});
    vector<vector<int>>visited(heights.size(), vector<int>(heights[0].size(), 0));
    visited[0][0] = 1;

    while (!q.empty()) {
        int r = q.front().first, c = q.front().second;
        q.pop();
        if (r == heights.size() - 1 && c == heights[0].size() - 1) return 1;
        for (int i = 0; i < 4; i++) {
            int nx = r + rowDir[i];
            int ny = c + colDir[i];
            if (nx >= 0 && nx < heights.size() && ny >= 0 && ny < heights[0].size() && abs(heights[nx][ny] - heights[r][c]) <= limit && visited[nx][ny]== 0) {
                q.push({nx, ny});
                visited[nx][ny] = 1;
            }
        }

    }

    return false;
}
    int minimumEffortPath(vector<vector<int>>& heights) {
        int l = 0;
        int r = 1e7;
        int res = r;
        while (l <= r) {
            int m = l + (r - l)/2;
            if (isValid(heights, m)) {
                res = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return res;
    }
};