class Solution {
public:
    int n;
    vector<int> arr;
    unordered_map<int , unordered_map<int, int>>mp;
    bool canCross(vector<int>& stones) {
        n = stones.size();
        arr = stones;

        return dfs(0, 0);


    }
    
    bool dfs(int i, int prev) {
        if (i == n - 1) return true;
        if (mp[i][prev] == 1) return false;

        for (int j = i + 1; j < n; j++) {
            if (abs(arr[j] - arr[i] - prev) <= 1) {
                if (dfs(j, arr[j] - arr[i])) {
                    return true;
                }
            }
        }
        mp[i][prev] = 1;
        return false;
    }
};