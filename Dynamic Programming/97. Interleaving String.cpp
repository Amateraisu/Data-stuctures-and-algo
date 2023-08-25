class Solution {
public:
    int n;
    int i, j;
    string goal;
    string str1;
    string str2;
    vector<vector<int>>dp;
    bool dfs(int ptr1, int ptr2) {
        
        if (ptr1 + ptr2 == n && ptr1 == i && ptr2 == j) return true;
        if (ptr1 >= i && ptr2 >= j) return false;
        if (dp[ptr1][ptr2] != -1) return dp[ptr1][ptr2];
        bool can = false;
        if (ptr1 < i && goal[ptr1 + ptr2] == str1[ptr1]) {
            can = can || dfs(ptr1 + 1, ptr2);
        }
        if (ptr2 < j && goal[ptr1 + ptr2] == str2[ptr2]) {
            can = can ||dfs(ptr1, ptr2 + 1);

        }
        dp[ptr1][ptr2] = can;
 
        return can;


    }
    bool isInterleave(string s1, string s2, string s3) {
        
        n = s3.length();
        i = s1.length();
        j = s2.length();
        dp = vector<vector<int>>(i + 1, vector<int>(j + 1, -1));
        goal = s3;
        str1 = s1, str2 = s2;
        if (i + j != n) return false;
        return dfs(0,0 );

    }
};