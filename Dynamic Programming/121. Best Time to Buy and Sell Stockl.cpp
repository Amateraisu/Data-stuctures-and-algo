class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // I can go from left to right
        int res = 0;
        int lowest = 1e9;
        for (int i = 0; i < prices.size(); i++) lowest = min(lowest, prices[i]), res = max(res, prices[i] - lowest);

        return res;
    }

};