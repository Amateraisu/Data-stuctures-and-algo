class Solution {
public:
    string removeTrailingZeros(string num) {
        int n = num.length();
        int m = n - 1;
        while (m >= 0 && num[m] == '0') m--;

        return num.substr(0, m + 1);

    }
};