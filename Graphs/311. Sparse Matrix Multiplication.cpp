class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& mat1, vector<vector<int>>& mat2) {
        int m = mat1.size();
        int n = mat2[0].size();
        int x = mat1[0].size();
        vector<vector<int>> res(m, vector<int> (n, 0));

        for (int i = 0; i < m; i++) {
            for (int k = 0; k < n; k++) {
                for (int j = 0; j < x; j++) {
                    res[i][k] += mat1[i][j] * mat2[j][k];

                }
            }
        }

        return res;

    }
};