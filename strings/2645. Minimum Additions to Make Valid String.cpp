class Solution {
public:
    int addMinimum(string word) {
        int res = 0;
        int ptr1 = 0;
        int n = word.size();
        unordered_set<char> seen;
        while (ptr1 < n) {
            char starting = word[ptr1];
            seen.clear();
            seen.insert(starting);
            int temp = ptr1 + 1;
            char prev = starting;
            while (temp < n && word[temp] > prev) {
                prev = word[temp];
                temp++;
            }

            res += 3 - (temp - ptr1);
            ptr1 = temp;

        }


        return res;


    }
};