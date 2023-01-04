class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # DFS APPROACH
        # O(N) time | O(N) space
        if n == 1:
            return 5

        MOD = 10**9 + 7

        @cache
        def dfs(current, currentLetter):
            if current == n:
                return 1
            best = 0
            if currentLetter == "a":
                best += dfs(current + 1, "e")
            elif currentLetter == "e":
                best += dfs(current + 1, "a")
                best += dfs(current + 1, "i")
            elif currentLetter == "i":
                best += dfs(current + 1, "a") + dfs(current + 1, "e") + \
                    dfs(current + 1, "o") + dfs(current + 1, "u")
            elif currentLetter == "o":
                best += dfs(current + 1, "i") + dfs(current + 1, "u")
            else:
                best += dfs(current + 1, "a")

            return best % MOD  # need to return % MOD here if not memory limit exceeded

        letters = ["a", "e", "i", "o", "u"]

        res = 0
        for letter in letters:
            res += dfs(1, letter)

        return res % MOD

        # ========== ITERATIVE APPROACH
        # if n == 1:
        #     return 5
        # MOD = 10 ** 9 + 7
        # dp = [[0 for i in range(5)] for j in range(n)]
        # # a e i o u
        # # 0 1 2 3 4
        # # initialize base case
        # # O(n) time
        # # O(n) space
        # # could optimize the time by specifying prev ptr
        # for i  in range(5):
        #     dp[0][i] = 1
        # # slowly build up the next case
        # for i in range(0, len(dp) - 1):
        #     # if its a
        #     for j in range(5):
        #         if j == 0: # a
        #             dp[i + 1][1] += dp[i][j]
        #         elif j == 1 : # e
        #             dp[i + 1][0] += dp[i][j]
        #             dp[i + 1][2] += dp[i][j]
        #         elif j == 2: # i
        #             dp[i + 1][0] += dp[i][j]
        #             dp[i + 1][1] += dp[i][j]
        #             dp[i + 1][3] += dp[i][j]
        #             dp[i + 1][4] += dp[i][j]
        #         elif j == 3: # o
        #             dp[i + 1][2] += dp[i][j]
        #             dp[i + 1][4] += dp[i][j]
        #         else : # u
        #             dp[i + 1][0] += dp[i][j]

        # # print(dp)
        # return sum(dp[-1]) % MOD
