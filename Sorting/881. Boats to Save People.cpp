class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int res = 0;
        int r = people.size() - 1;
        int l = 0;
        while (l <= r) {
            int f = people[l], s = people[r];
            if (f + s <= limit) {
                l++;
                r--;
            } else {
                r--;
            }
            res++;
        }
        return res;
    }
};
