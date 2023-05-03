class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1;
        unordered_set<int> set2;

        for (int num: nums1) set1.insert(num);
        for (int num: nums2) set2.insert(num);
        vector<vector<int>> res;
        unordered_set<int> res1;
        unordered_set<int> res2;
        for (auto num: nums1) {
            if (set2.find(num) == set2.end()) res1.insert(num);
        }
        for (auto num: nums2) {
            if (set1.find(num) == set1.end()) res2.insert(num);
        }
        vector<int> res3(res1.begin(), res1.end());
        vector<int> res4(res2.begin(), res2.end());


        res.push_back(res3);
        res.push_back(res4);
        return res;



    }
};