class Solution {
public:
    int maximumCandies(vector<int>& candies, long long k) {
        int n = candies.size();
        long long t = 0;
        for (int i = 0; i < n ; i++) t+=candies[i];
        if (t < k) return 0;
        int l = 1;
        int r = *max_element(candies.begin(), candies.end());
        int res = l;
        while (l <= r) {
            int m = l + (r - l)/2;
            if (isValid(m, candies, k)) {
                res = m;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return res;

    }

    int isValid(int m ,vector<int>& candies, long long k ) {
        long long t = 0;
        long long g = m * k;
        for (int i = 0; i < candies.size(); i++) {
            if (candies[i] >= m) {
                t += floor(candies[i] / m);
            }
        }
        return t >= k;

    }
};