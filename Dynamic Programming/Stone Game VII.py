class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        prefixSums = [0] * len(stones)
        
        prefixSums[0] = stones[0]
        for i in range(1, len(stones)):
            prefixSums[i] = prefixSums[i - 1] + stones[i]
        # print(prefixSums)
        
        cache = {}
        def dfs(left, right, isAliceTurn):
            
            if left == right:
                return 0 
            
            
            if (left, right, isAliceTurn) in cache:
                return cache[(left, right, isAliceTurn)]
            
            
            if isAliceTurn:
                # take from right 
                temp = float("-inf")
                # print("1")
                if left == 0:
                
                    temp = max(temp,  dfs(left, right - 1, not isAliceTurn) + prefixSums[right - 1])
                else:
                    temp = max(temp, dfs(left, right - 1, not isAliceTurn) + prefixSums[right - 1] - prefixSums[left - 1])
                
                # take from left 
                
                temp = max(temp, dfs(left + 1, right, not isAliceTurn) + prefixSums[right] - prefixSums[left])
            else:
                # take from right 
                temp = float("inf")
                if left == 0:
                    temp = min(temp, dfs(left, right - 1, not isAliceTurn) - prefixSums[right - 1])
                else:
                    temp = min(temp, dfs(left, right - 1, not isAliceTurn) - prefixSums[right - 1] + prefixSums[left - 1])
                
                
                
                # take from left 
                
                temp = min(temp, dfs(left + 1, right, not isAliceTurn) - (prefixSums[right] - prefixSums[left]))
            
            cache[(left, right, isAliceTurn)] = temp 
            
            return cache[(left, right, isAliceTurn)]
            
        return dfs(0, len(stones) - 1, True)