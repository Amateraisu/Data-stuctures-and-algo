class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        matrix = self.createMatrix(m, n)
        
        
        
        return matrix[-1][-1]
    def createMatrix(self, m, n):
        dp = [[ 0 for i in range(n)] for j in range(m)]
        
        dp[0][0] = 0 
        for i in range(1, n):
            dp[0][i] = 1 
            
        for j in range(1, m):
            dp[j][0] = 1 
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        return dp