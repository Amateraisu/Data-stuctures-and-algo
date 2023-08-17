class Solution {
public:
    vector<int> getModifiedArray(int n, vector<vector<int>>& updates) {
        vector<int>res(n, 0);
        vector<int>diff(n + 1, 0);
        for (auto update: updates) {
            diff[update[0]] += update[2];
            diff[update[1] + 1] -= update[2];
        }
        res[0] = diff[0];
        for (int i = 1 ;i < n; i++) {
            res[i] = res[i - 1] + diff[i];
        }
        return res;

    }
};