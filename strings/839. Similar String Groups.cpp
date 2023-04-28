class Solution {

public:
    int numSimilarGroups(vector<string>& strs) {
        int n = strs.size();
        vector<int> parents(n, 1);

        vector<int> ranks(n, 1);
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
        int res = n;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (same(i, j, strs)) {
                    res += uf(i, j, parents, ranks);
                }


            }
        }

        return res;

    }

    bool same(int i, int j, vector<string>& strs) {
        int diff = 0;
        for (int z = 0; z < strs[i].length(); z++) {
            if (strs[i][z] != strs[j][z]) {
                diff++;
            }
        }

        if (diff == 2 || diff == 0) return true;

        return false;
    }


    int find(int x, vector<int>& parents) {
        while (x != parents[x]) {
            x = parents[x];
        }
        return x;
    }

    int uf(int i, int j, vector<int>& parents, vector<int>& ranks) {
        int par1 = find(i, parents);
        int par2 = find(j, parents);
        if (par1 == par2) {
            return 0;
        }

        if (ranks[par1] > ranks[par2]) {
            parents[par2] = par1;
            ranks[par1] += ranks[par2];
            ranks[par2] = ranks[par1];
        } else {
            parents[par1] = par2;
            ranks[par2] += ranks[par1];
            ranks[par1] = ranks[par2];
        }

        return -1;





    }




};