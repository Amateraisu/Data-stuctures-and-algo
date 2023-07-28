class Solution {
public:
    int minMoves(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;
        // with every increment, I can increment n - 1 elements by 1
        // which means that I can always make the array equal no matter the size of the array
        // but on the contrary, if I remove the decrement the maximum number by 1,
        int mini = *min_element(nums.begin(), nums.end());
        int res = 0;
        for (int m : nums) res += m - mini;
        return res;

    }
};