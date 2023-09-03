class Solution {
public:
    int minimumOperations(string num) {
      vector<string> vec = {"00", "25", "50", "75"};
      int ret = num.size();
      for (int i = 0; i < num.size(); i++) {
        if (num[i] == '0') {
          ret = (int)num.size() - 1;
          break;
        }
      }
      for (auto t: vec) {
        int j = num.size() - 1;
        while (j >= 0 && num[j] != t[1]) j--;
        if (j == -1) continue;
        j--;
        while (j >= 0 && num[j] != t[0]) j--;
        if (j == -1) continue;
        j--;
        ret = min(ret, (int)num.size() - 1 - j - 2);
      }
      return ret;
    }
};