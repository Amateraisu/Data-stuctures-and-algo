class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // basically the lowest poitn and the next highest point
        int res = 0;
        int c = INT_MAX;
        for (int price :prices) {
            if (price < c) c = price;
            res = max(res, price - c);
        }
        return res;

    }
};