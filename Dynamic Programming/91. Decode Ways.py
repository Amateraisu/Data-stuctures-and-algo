class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1 and s[0] == '0':
            return 0
        
        dp = [0 for num in range(len(s)+1)]
        if s[-1] == '0':
            dp[-1] = 1 
            dp[-2] = 0
        else:
            
            dp[-1] = 1
            dp[-2] = 1

        for i in reversed(range(len(dp)-2)):
            if s[i] == '0':
                continue
            
            if int((s[i:i+2])) <= 26:
                dp[i] = dp[i+1] + dp[i+2]

            else:
                dp[i] = dp[i+1]


        return dp[0]