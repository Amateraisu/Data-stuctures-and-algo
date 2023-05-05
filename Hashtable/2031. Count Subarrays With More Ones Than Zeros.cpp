class Solution {
public:
    int subarraysWithMoreZerosThanOnes(vector<int>& nums) {
        unordered_map<int, int> count;
        const int MOD = 1e9 + 7;
        count[0] = 1;
        int prev = 0;
        int res = 0;
        int total = 0;
        for (int num : nums) {
            if (num == 1) {
                total += 1;
                prev += count[total - 1];
            } else {
                total -= 1 ;
                prev -= count[total];
            }
            res = (res + prev) % MOD;
            count[total]++;

        }

        return res % MOD ;

    }
};