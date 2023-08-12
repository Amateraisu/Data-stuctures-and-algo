class Solution {
public:
    long long countVowels(string word) {
        long long res =0;
        vector<char>vowels = {'a', 'e', 'i', 'o', 'u'};
        long long n = word.length();
        for (long long i =0; i < n; i++) {
            if (word[i] == 'a' || word[i] == 'e'|| word[i] == 'i' || word[i] == 'o' || word[i] == 'u') {
                long long t = (i + 1) * (n - i);
                res += t;
            }
        }

        return res;

    }
};