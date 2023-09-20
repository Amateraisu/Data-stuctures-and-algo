class Solution {
public:
    int find(int a , int b) {
        if (b == 0) return a;
        return find(b, a % b);
    }
    int findGCD(vector<int>& nums) {
        int maxi = *max_element(nums.begin(), nums.end());
        int mini = *min_element(nums.begin(), nums.end());
        return find(mini ,maxi);

    }
};