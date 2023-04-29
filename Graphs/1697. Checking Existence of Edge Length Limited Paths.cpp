class Solution {
public:
    bool static compare1(vector<int>& a, vector<int>& b) {
        return a[3] < b[3];
    }
    bool static compare2(vector<int>& a, vector<int>& b) {
        return a[2] < b[2];
    }

    int find(int node, vector<int>& parents) {
        if (parents[node] != node) {
            parents[node] = find(parents[node], parents);
        }

        return parents[node];

    }
    void u(int n1, int n2, vector<int>& parents) {
        int p1 = find(n1, parents);
        int p2 = find(n2, parents);

        if (p1 == p2) {
            return;
        }

        parents[p2] = p1;
        return;
    }


    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
        vector<int> parents(n, 0);
        vector<vector<int>> newQueries;
        vector<bool> res(queries.size(), false);

        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
        for (int i = 0; i < queries.size(); i++) {
            newQueries.push_back({queries[i][0], queries[i][1], queries[i][2], i});
        }

        sort(newQueries.begin(), newQueries.end(), compare2);
        sort(edgeList.begin(), edgeList.end(), compare2);

        int ptr1 = 0 ;
        for (int i = 0; i < newQueries.size(); i++) {
            while (ptr1 < edgeList.size() && edgeList[ptr1][2] < newQueries[i][2]) {
                u(edgeList[ptr1][0], edgeList[ptr1][1], parents);
                ptr1++;
            }

            res[newQueries[i][3]] = find(newQueries[i][0], parents) == find(newQueries[i][1], parents);

        }

        return res;


    }




};