class Solution {
public:
int maxIncreasingCells(vector<vector<int>>& mat) {
    vector<array<int, 3>> vij;
    int m = mat.size(), n = mat[0].size();
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            vij.push_back({mat[i][j], i, j});
    sort(begin(vij), end(vij));
    vector<int> v_r(m, INT_MIN), v_c(n, INT_MIN);
    vector<vector<int>> cnt_r(m, vector<int>(2)), cnt_c(n, vector<int>(2));
    for (auto [v, i, j] : vij) {
        int cnt = max(cnt_r[i][v == v_r[i]], cnt_c[j][v == v_c[j]]);
        if (v > v_r[i])
            cnt_r[i][1] = cnt_r[i][0];
        if (v > v_c[j])
            cnt_c[j][1] = cnt_c[j][0];
        cnt_r[i][0] = max(1 + cnt, cnt_r[i][0]);
        cnt_c[j][0] = max(1 + cnt, cnt_c[j][0]);
        v_r[i] = v_c[j] = v;
    }
    return (*max_element(begin(cnt_r), end(cnt_r)))[0];
}
};