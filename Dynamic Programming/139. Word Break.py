class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for letter in range(len(s)+1)]
        dp[-1] = True
        
        for index in range(len(s)-1, -1, -1):
            for word in wordDict:
                if s[index : index + len(word)] == word:
                    dp[index] = dp[index + len(word)]
                if dp[index]:
                    break
        return dp[0]