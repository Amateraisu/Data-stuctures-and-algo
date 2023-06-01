class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if (grid[0][0] == 1) return -1;
        int n = grid.size();
        queue<vector<int>> q;
        vector<vector<int>> directions = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

        q.push({0, 0, 1});
        grid[0][0] = -1;

        while (!q.empty()) {
            int r = q.front()[0];
            int c = q.front()[1];
            int cost = q.front()[2];

            if (r == n -1 && c == n - 1) return cost;
            q.pop();

            for (auto direct : directions) {
                int nr = r + direct[0];
                int nc = c + direct[1];
                if (nr >= 0 && nr <= n - 1 && nc >= 0 && nc <= n - 1 && grid[nr][nc] == 0) {
                    grid[nr][nc] = -1;
                    q.push({nr, nc, cost + 1});

                }
            }



        }

        return -1;


    }
};