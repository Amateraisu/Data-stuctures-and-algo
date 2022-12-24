class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007
        
        # handle base case scenarios
        if n <= 2:
            return n

        # f[k]: number of ways to "fully cover a board" of width k
        f = [0] * (n + 1)  
        
        # p[k]: number of ways to "partially cover a board" of width k
        p = [0] * (n + 1)  
        
        # initialize f and p with results for the base case scenarios
        f[1] = 1
        f[2] = 2
        p[2] = 1
        
        for k in range(3, n + 1):
            f[k] = (f[k - 1] + f[k - 2] + 2 * p[k - 1]) % MOD
            p[k] = (p[k - 1] + f[k - 2]) % MOD
        return f[n]