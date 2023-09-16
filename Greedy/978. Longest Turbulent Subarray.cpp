class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int res = 0;
        int cur = 1;
        for (int i = 0; i < arr.size(); i++) {
            res = max(res, cur);
            if (i % 2 == 0) {
                if (i < arr.size() - 1 && arr[i + 1] > arr[i]) {
                    cur++;
                } else {
                    cur = 1;
                }

            }
            if (i % 2 != 0) {
                if (i < arr.size() - 1 && arr[i + 1] < arr[i]) {
                    cur++;
                } else {
                    cur = 1;
                }
            }
        }
        cur = 1;
        for (int i = 0; i < arr.size(); i++) {
            res = max(res, cur);
            if (i % 2 != 0) {
                if (i < arr.size() - 1 && arr[i + 1] > arr[i]) {
                    cur++;
                } else {
                    cur = 1;
                }

            }
            if (i % 2 == 0) {
                if (i < arr.size() - 1 && arr[i + 1] < arr[i]) {
                    cur++;
                } else {
                    cur = 1;
                }
            }
        }

        return res;
    }
};
