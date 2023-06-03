class Solution:
    MOD = int(1e9 + 7)

    def numDecodings(self, s):
        n = len(s)
        dp = [-1] * n
        return self.dfs(0, dp, s)

    def dfs(self, index, dp, s):
        if index == len(s):
            return 1
        if index > len(s):
            return 0
        if s[index] == '0':
            return 0
        if dp[index] != -1:
            return dp[index]

        r = 0
        if s[index] == '*':
            r = (r + self.dfs(index + 1, dp, s) * 9) % self.MOD
        else:
            r = (r + self.dfs(index + 1, dp, s)) % self.MOD

        r %= self.MOD
        if index <= len(s) - 2:
            if s[index + 1] == '*':
                if s[index] == '1':
                    r = (r + self.dfs(index + 2, dp, s) * 9) % self.MOD
                elif s[index] == '2':
                    r = (r + self.dfs(index + 2, dp, s) * 6) % self.MOD
                elif s[index] == '*' and s[index + 1] == '*':
                    r = (r + self.dfs(index + 2, dp, s) * 15) % self.MOD
            elif s[index] != '*' and int(s[index:index+2]) <= 26:
                r = (r + self.dfs(index + 2, dp, s)) % self.MOD
            elif s[index] == '*' and s[index + 1] != '*':
                if int(s[index + 1]) <= 6:
                    r = (r + self.dfs(index + 2, dp, s)) % self.MOD
                if int(s[index + 1]) <= 9:
                    r = (r + self.dfs(index + 2, dp, s)) % self.MOD

        r %= self.MOD
        dp[index] = r
        return r
