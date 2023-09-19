class Solution {
public:
    double myPow(double x, int n) {
        double res = 1;
        double base = x;
        int t = abs(n);
        while (t > 0) {
            if (t % 2 == 1) {
                res = res * base;
            }
            t/=2;
            base *= base;
        }
        if (n < 0) {
            return 1/res;
        }
        return res;
    }
};
