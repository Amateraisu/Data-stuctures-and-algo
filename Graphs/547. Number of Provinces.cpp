class Solution {
public:

    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<int> parents(n, 1);
        for (int i = 0; i < n ; i++) parents[i] = i;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (isConnected[i][j]) uf(i, j, parents);
            }
        }

        int res = 0;
        unordered_set<int> visited;
        for (int i = 0; i < n; i++) {
            visited.insert(find(i, parents));
        }
        return visited.size();

    }

    int find(int n, vector<int>& parents) {
        if (parents[n] != n) parents[n] = find(parents[n], parents);

        return parents[n];
    }

    void uf(int n1, int n2, vector<int>& parents) {
        int p1 =find(n1, parents);
        int p2 = find(n2, parents);
        if (p1 == p2) return;
        parents[p1] = p2;

    }
};