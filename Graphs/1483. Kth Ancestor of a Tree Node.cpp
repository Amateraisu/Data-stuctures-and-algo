class TreeAncestor {
public:
    int bits = 32;
    vector<vector<int>>dp;
    TreeAncestor(int n, vector<int>& parent) {
        dp = vector<vector<int>>(n + 1, vector<int>(32, 0));
        for (int i = 2; i <= n; i++) {
            dp[i][0] = parent[i - 1] + 1;
        }
        for (int j = 1; j < bits; j++) {
            for (int i = 2; i<= n; i++) {
                dp[i][j] = dp[dp[i][j - 1]][j - 1];
            }
        }
    }

    int getKthAncestor(int node, int k) {
        int res = node + 1;
        for (int j = 0; j < bits; j++) {
            if (k & (1 << j)) {
                res =  dp[res][j];
            }
        }
        if (res == 0) return -1;
        return res - 1;
    }
};