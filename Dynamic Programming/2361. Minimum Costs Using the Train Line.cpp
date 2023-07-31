class Solution {
public:
    vector<long long> minimumCosts(vector<int>& regular, vector<int>& express, int c) {
        int n =regular.size();
        vector<long long> dp1(n + 1, 1e9);
        vector<long long> dp2(n + 1, 1e9);
        dp1[0] = 0;
        dp2[0] = c;
        for (int i = 1; i < n + 1; i++) {
            dp1[i] = min(dp1[i - 1] + regular[i - 1], dp2[i - 1] + express[i - 1]);
            dp2[i] = min(dp2[i - 1] + express[i - 1], dp1[i - 1] + regular[i - 1] + c);
        }
        vector<long long>res;
        for (int i = 1; i < n + 1 ; i++) res.push_back(min(dp1[i], dp2[i]));

        return res;
    }
};