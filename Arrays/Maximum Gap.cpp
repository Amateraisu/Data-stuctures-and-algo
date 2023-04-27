class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if (nums.size() < 2) {
            return 0;
        }

        int n = nums.size();
        int mini = *min_element(nums.begin(), nums.end());
        int maxi = *max_element(nums.begin(), nums.end());
        if (maxi == mini) {
            return 0;
        }

        int bucket_size = max(1, (maxi - mini) / (n - 1));
        int bucket_count = (maxi - mini) / bucket_size + 1;

        vector<vector<int>> buckets(bucket_count, vector<int>{INT_MAX, INT_MIN});

        for (int num : nums) {
            int i = (num - mini) / bucket_size;
            buckets[i][0] = min(buckets[i][0], num);
            buckets[i][1] = max(buckets[i][1], num);
        }

        // buckets.erase(remove_if(buckets.begin(), buckets.end(), [](const vector<int>& bucket) {
        //     return bucket[0] == INT_MAX && bucket[1] == INT_MIN;
        // }), buckets.end());
        vector<vector<int>> bucc;
        for (auto b : buckets) {
            if (b[0] != INT_MAX && b[1] != INT_MIN) {
                bucc.push_back(b);
            }
        }

        int res = 0;
        int prev_max = bucc[0][1];
        for (int i = 1; i < bucc.size(); i++) {
            res = max(res, bucc[i][0] - prev_max);
            prev_max = bucc[i][1];
        }

        return res;
    }
};