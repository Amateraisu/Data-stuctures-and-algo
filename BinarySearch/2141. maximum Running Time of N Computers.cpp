class Solution {
public:
    long long maxRunTime(int n, vector<int>& batteries) {
        long long l = 1;
        long long r = 0;
        for (int i = 0; i < batteries.size(); i++) r += batteries[i];
        long long res = 1;
        while (l <= r) {
            long long mid = l + (r - l)/2;
            if (isValid(mid, batteries, n)) {
                l = mid + 1;
                res = mid;
            } else {
                r = mid - 1;
            }
        }

        return res ;
    }

    int isValid(long long m, vector<int>& batteries, int n) {
        long long c = 0;
        for (int i = 0; i < batteries.size(); i++) {
            c += min((long long)batteries[i], m);
        }
        if (c >= (long long) m * n) {
            return 1;
        }
        return 0;


    }
};