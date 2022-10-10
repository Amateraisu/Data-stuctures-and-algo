from collections import defaultdict
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        ispal = [[False]*n for _ in range(n)] # dp of palindrome

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j]:
                    ispal[i][j] = True if j-i<=2 else ispal[i+1][j-1]

        for i in range(1,n-1):
            for j in range(i,n-1):
                if ispal[i][j]:
                    if ispal[0][i-1] and ispal[j+1][n-1]: return True

        return False