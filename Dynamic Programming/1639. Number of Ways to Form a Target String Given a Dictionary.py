class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        MOD = 10 ** 9 + 7
        n = len(target)
        # I need to reduce the time complexity of searching for the correct character

        dp = [[0 for i in range(26)] for j in range(len(words[0]))]
        for word in words:
            for i, char in enumerate(word):
                dp[i][ord(char) - ord('a')] += 1

        @cache
        def dfs(i, k):
            if i == n:
                return 1
            if k == len(words[0]):
                return 0

            currentChar = target[i]
            best = 0

            best += dfs(i + 1, k + 1) * dp[k][ord(currentChar) - ord('a')]
            best += dfs(i, k + 1)
            return best % MOD

        return dfs(0, 0)
