class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:

        n = len(types)
        MOD = 10 ** 9 + 7

        dp = [[0 for i in range(n + 1)] for j in range(target + 1)]
        # let dp[i][j] be defined as the number of ways to reach score[i] with piles[j]
        # so the base case is that dp[0][0] = 1 because there is exatly 1 way to get a point of 0 with no piles
        # we have a certain score, target, to hit
        # so we want to make sure dp[i][j] += dp[i - someScore][j] + count at the (j-1)th pile WHERE someScore = count * score of that pile

        for i in range(n + 1):
            dp[0][i] = 1

        for i in range(1, target + 1):
            for j in range(1, n + 1):
                currentPile = types[j - 1]
                for count in range(currentPile[0] + 1):  # we can choose to take 0 ~ all the question types
                    score = count * currentPile[1]
                    if i - score >= 0:
                        dp[i][j] += dp[i - score][j - 1] % MOD

                        # print(dp)
        return dp[target][n] % MOD

        # DFS
        # TIME: O(mn)
        # n = len(types)
        # MOD = 10**9 + 7
        # @cache
        # def dfs(current, current_pile):
        #     if current == target:
        #         return 1
        #     if current_pile == n:
        #         return 0
        #     if current > target:
        #         return 0
        #     best = 0
        #     for i in range(types[current_pile][0] + 1):
        #         # choose to take a certain amount of qn in this type
        #         gain = types[current_pile][1] * i
        #         best += dfs(current + gain, current_pile + 1)

        #     return best % MOD

        # return dfs(0, 0) % MOD