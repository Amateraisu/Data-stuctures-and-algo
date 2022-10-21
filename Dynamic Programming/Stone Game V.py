class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        # BASICALLY, BINARY SEARCH IT.
        if len(stoneValue) == 1:
            return 0
        prefixSums = [0] * len(stoneValue)
        prefixSums[0] = stoneValue[0]
        
        for i in range(1, len(stoneValue)):
            prefixSums[i] = prefixSums[i - 1] + stoneValue[i]
            
        
        cache = {}
        
        def dfs(left, right):
            if left == right:
                return 0 
            
            if (left, right) in cache:
                return cache[(left, right)]
            
            temp = 0 
 
            # maybe we can use binary search to determine the range to cut 
            # so lets say 
            if left == 0:
                leftCum = 0 
            else:
                leftCum = prefixSums[left - 1]
            i = binarySearch(0, prefixSums[right] - leftCum)
            

            leftScore = prefixSums[i] - leftCum
            rightScore = prefixSums[right] - prefixSums[i]
            if leftScore == rightScore:
                temp = max(temp, dfs(left, i) + leftScore , dfs(i + 1, right) + leftScore)


            elif leftScore <= rightScore:
                temp = max(temp, dfs(left, i) + leftScore)

            else : # right score < leftscore 
                temp = max(temp, dfs(i + 1, right) + rightScore)
                
                
                
            cache[(left, right)] = temp 
            
            
            return cache[(left, right)]
        
        
        return dfs(0, len(stoneValue) - 1)
        
        
        
def binarySearch(l ,r):
    resIndex = None
    res = float("inf")
    while l <= r:
        if canSplit()
        
        
        
        
        
        
        
        
        
        
        
        
        # O(n^3) TLE 
#         if len(stoneValue) == 1:
#             return 0
#         prefixSums = [0] * len(stoneValue)
#         prefixSums[0] = stoneValue[0]
        
#         for i in range(1, len(stoneValue)):
#             prefixSums[i] = prefixSums[i - 1] + stoneValue[i]
            
        
#         cache = {}
        
#         def dfs(left, right):
#             if left == right:
#                 return 0 
            
#             if (left, right) in cache:
#                 return cache[(left, right)]
            
#             temp = 0 
 
#             # maybe we can use binary search to determine the range to cut 
#             # so lets say 
#             for i in range(left, right):
#                 if left == 0:
#                     leftCum = 0 
#                 else:
#                     leftCum = prefixSums[left - 1]
#                 leftScore = prefixSums[i] - leftCum
#                 rightScore = prefixSums[right] - prefixSums[i]
#                 if leftScore == rightScore:
#                     temp = max(temp, dfs(left, i) + leftScore , dfs(i + 1, right) + leftScore)
                
                
#                 elif leftScore <= rightScore:
#                     temp = max(temp, dfs(left, i) + leftScore)
                    
#                 else : # right score < leftscore 
#                     temp = max(temp, dfs(i + 1, right) + rightScore)
                
                
                
#             cache[(left, right)] = temp 
            
            
#             return cache[(left, right)]
        
        
#         return dfs(0, len(stoneValue) - 1)
    