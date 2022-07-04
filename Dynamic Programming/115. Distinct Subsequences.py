class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
        for j in range(len(t) + 1):
            dp[len(s)][j] = 0
        
        for i in range(len(s) + 1):
            dp[i][len(t)] = 1 
            
            
            

            
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                print(i, j)
                
                dp[i][j] = dp[i+1][j]
                
                if s[i] == t[j]:
                    
                    dp[i][j] += dp[i+1][j + 1]

                    
        return dp[0][0]