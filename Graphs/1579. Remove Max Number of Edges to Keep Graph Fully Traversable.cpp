class Solution {
public:

    bool static compare(vector<int>& a, vector<int>& b) {
        return  a[0] > b[0];
    }

    int find(int n, vector<int>& parents) {
        if (parents[n] != n) {
            parents[n] = find(parents[n], parents);
        }

        return parents[n];
    }

    bool uf(int n1, int n2, vector<int>& parents, vector<int>& ranks) {
        int p1 = find(n1, parents);
        int p2 = find(n2, parents);

        if (p1 == p2) return false;

        if (ranks[p1] > ranks[p2]) {
            ranks[p1] += ranks[p2];
            ranks[p2] = ranks[p1];
            parents[p2] = p1;
        } else {
            ranks[p2] += ranks[p1];
            ranks[p1] = ranks[p2];
            parents[p1] = p2;
        }

        return true;
    }



    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        vector<int> a_pars(n, 0);
        vector<int> a_ranks(n, 1);

        vector<int> b_pars(n, 0);
        vector<int> b_ranks(n, 1);

        int res = 0;

        for (int i = 0; i < n ; i++) {
            a_pars[i] = i;
            b_pars[i] = i;
        }

        sort(edges.begin(), edges.end(), compare);

        for (auto edge : edges) {
            edge[1]--;
            edge[2]--;
            if (edge[0] == 3) {
                if (!uf(edge[1], edge[2], a_pars, a_ranks) || !uf(edge[1], edge[2], b_pars, b_ranks)) {
                    res++;
                }

            } else if (edge[0] == 1) {
                if (!uf(edge[1], edge[2], a_pars, a_ranks)) {
                    res++;
                }

            } else {
                if (!uf(edge[1], edge[2], b_pars, b_ranks)) {
                    res++;
                }

            }
        }

        unordered_set<int> a_visited;
        unordered_set<int> b_visited;

        for (int i = 0; i < n; i++) {
            int p1 = find(a_pars[i], a_pars);
            int p2 = find(b_pars[i], b_pars);
            a_visited.insert(p1);
            b_visited.insert(p2);
        }


        if (a_visited.size() > 1 || b_visited.size() > 1) {
            return -1;
        }


        return res;





    }
};