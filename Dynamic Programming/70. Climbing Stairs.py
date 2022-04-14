class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for num in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for num in range(2,n+1):
            dp[num] = dp[num-1] + dp[num-2]
            
        return dp[-1]