class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int res = 0;
        int n = 0;
        for (char c : s) {
            if (c == '0') {
                res = min(n , res + 1);
            } else {
                n++;
            }
        }

        return res;

    }
};