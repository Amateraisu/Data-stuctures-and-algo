class Solution {
public:
    int bestClosingTime(string customers) {
        int l = 0;
        int r = customers.length() + 1;
        int n = customers.length();
        vector<int> close(n + 1, 0);
        vector<int> open(n + 1, 0);
        int cur = 0;
        int cur2 = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (customers[i] == 'Y') cur++;
            close[i] = cur;
        }
        for (int i = 0; i < n + 1; i++) {
            if (customers[i] == 'N') cur2++;
            open[i] = cur2;
        }

        int res = -1;
        int t = 1e5;

        for (int i = 0; i <= n ; i++) {
            int cost = close[i];
            if (i - 1 >= 0) {
                cost = close[i] + open[i - 1];
            }
            if (cost < t) t = cost, res = i;
        }

        return res;

    }
};