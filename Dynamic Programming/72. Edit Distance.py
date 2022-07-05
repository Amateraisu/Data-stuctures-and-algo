class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf") for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        
        dp[0][0] = 0 
        
        # row 
        for i in range(len(word1) + 1):
            dp[i][0] = i

        for j in range(len(word2) + 1):
            dp[0][j] = j 

        for i in range(1,len(word1) + 1):
            for j in range(1,len(word2) + 1):
                toAdd = 0
                if word2[j - 1] != word1[i - 1]:
                    toAdd += 1 
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + toAdd)
                
                
                
                
        return dp[-1][-1]