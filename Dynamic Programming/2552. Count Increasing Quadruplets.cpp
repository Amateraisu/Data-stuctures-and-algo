using ll = long long;
class Solution {
public:
    long long countQuadruplets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> gt(n, vector<int>(n, 0)), lt(n, vector<int>(n, 0));
        //gt  for elemnts l 
        //lt for elemnts i lt[i][j] represents all the numbers lesser than nums[j] from range i to j 
        // gt for elemnts l, gt[i][j] represents for all numbers from range i to j greater than nums[i]
        for (int i = 0; i < n; i++) {
            int cur = 0;
            for (int j = i -1; j >=0 ; j--) {
                if (nums[j] < nums[i]) cur++;
                lt[j][i] = cur;
            }
        }
        for (int i = 0; i < n; i++) {
            int cur =0 ;
            for (int j = i + 1; j < n; j++) {
                if (nums[j] > nums[i]) cur++;
                gt[i][j] = cur;
            }
        }




        long long res = 0;
        for (int j = 1; j < n - 2; j++) {
            for (int k = j + 1; k < n - 1; k++) {
                if (nums[j] > nums[k]) {
                    ll i = lt[0][k] - lt[j][k];
                    ll l = gt[j][n -1] - gt[j][k];
                    res += i * l;
                }
            }
        }
        return res;
    }
};