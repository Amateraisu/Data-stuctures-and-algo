class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        

  
        n = len(s)
        # cache = {}
        MOD = 10**9 + 7
        @cache
        def dfs(currentIndex):
            if currentIndex == n:

                return 1

            # if currentIndex in cache:
            #     return cache[currentIndex]
            
            temp = 0
            currentNum = 0
            for i in range(currentIndex, n):
                currentNum = currentNum * 10 + int(s[i])

                # print(currentNum, "test", currentIndex, i)
                if currentNum <= k :
                    if (i ==n-1 or s[i+1]!="0"):

                        temp += dfs(i + 1)
                else:
                    break
                    
            # cache[currentIndex] = temp
            
            return temp % MOD
        
        return dfs(0) 