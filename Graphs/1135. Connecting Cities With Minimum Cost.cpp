class Solution {
public:
    static bool com(vector<int>& a, vector<int>& b) {
        return a[2] < b[2];
    }
    int find(int node, vector<int>& parents) {
        if (parents[node] != node) parents[node] = find(parents[node], parents);


        return parents[node];
    }

    int uf(int n1, int n2, int c, vector<int>& parents) {
        int p1 = find(n1, parents);
        int p2 = find(n2, parents);
        if (p1 == p2) return 0;
        parents[p1] = p2;
        return c;

    }


    int minimumCost(int n, vector<vector<int>>& connections) {
        sort(connections.begin(), connections.end(), com);
        vector<int> parents(n, 0);
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
        int res = 0;
        for (auto connect: connections) {
            res += uf(connect[0] - 1, connect[1] - 1, connect[2], parents);
        }
        unordered_set<int> visited;
        for (int par: parents) {
            visited.insert(find(par, parents));
        }
        if (visited.size() > 1) {
            return -1;
        }
        return res;
    }
};