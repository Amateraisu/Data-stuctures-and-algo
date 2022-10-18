class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        
        # O(n^2k) time ~ O(n^3) time 
        
        # O(n * k) time 
        cache = {}
        prefixTable = {}
        def dfs(index, currentk):
            if (index, currentk) in cache:
                return cache[(index, currentk)]
            
            
            if currentk == 0:
                return 1 
            if index == n:
                return 0 
            

            
            temp = 0 
            temp += dfs(index + 1 , currentk)
            
            # O(n) time to retrieve 
            # here, so what we are doing is retrieving from every state beyond our current state 
            # what if when we were calculating our future states, we saved it into one hashtable ? 
            
            # currently : dfs(index, x)
            # calculating: dfs(index + 1, x - 1) , dfs(index + 2, x - 1), dfs(index + 3, x - 1)

                 # dont make a line 
            temp += prefixSum(index + 1, currentk - 1)
            cache[(index, currentk)] = temp 
            
            return cache[(index, currentk)] 
        def prefixSum(end, remain):
            if end == n:
                return 0 
            if (end, remain) in prefixTable:
                return prefixTable[(end, remain)]
            ans = 0 
            ans = dfs(end, remain) + prefixSum(end + 1, remain)
            prefixTable[(end, remain)] = ans 
            
            return ans
        
        MOD = 10**9 + 7 
        return dfs(0, k) % MOD