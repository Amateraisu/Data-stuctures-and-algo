class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        #initialise base case 
        rows = len(dp)
        columns = len(dp[0])
        
        for row in range(1,rows):

            for col in range(1,columns):
                
                if text1[col-1] == text2[row-1] :
                    #find the max and + 1 
                    dp[row][col] = dp[row-1][col-1] + 1   

                else:
                    dp[row][col] = max(dp[row-1][col-1], dp[row-1][col], dp[row][col-1])
                    

        return dp[-1][-1]