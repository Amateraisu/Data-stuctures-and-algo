class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        int l = 0;
        int r = n - 1;

        while (l < r) {

            int total = numbers[l] + numbers[r];
            if (total == target) {
                return {l + 1, r + 1};
            } else if (total < target) {
                l++;

            } else {
                r--;
            }
        }

        return {-1, -1};

    }
};