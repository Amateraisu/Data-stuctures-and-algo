class Solution {
public:
    int maxVowels(string s, int k) {
        unordered_set<char> vowels({'a', 'e','i','o','u'});
        int l = 0;
        int res = 0;
        int c = 0;
        int n = s.length();
        for (int i =0; i < n; i++) {
            if (i - l + 1 > k) {
                if (vowels.find(s[l]) != vowels.end()) {
                    c--;
                }
                l++;
            }
            if (vowels.find(s[i]) != vowels.end()) {
                c++;

            }
            res = max(res, c);

        }


        return res;

    }
};