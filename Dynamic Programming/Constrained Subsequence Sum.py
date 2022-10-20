from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # optimized 1D dp 
        
        dp = [float("-inf")] * len(nums)
        res = float("-inf")
        
        queue = deque()
        
        for right in range(len(nums)):
            if right == 0:
                dp[right] = nums[right]
                queue.append([dp[right], 0])
                
            else:
                # make sure its a valid queue first 
                while queue and queue[0][-1] < right - k:
                    queue.popleft()
                    
                dp[right] = max(queue[0][0] + nums[right], nums[right])
                # so when I have the result, make it a monotonically decreasing queue 
                while queue and queue[-1][0] < dp[right]:
                    queue.pop()
                queue.append([dp[right], right])
                
            res = max(res, dp[right])
            # print("Index", right)
            # print("result", res)
            # print("queue", queue)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # iterative 1D dp 
#         # O(n^2) TLE 
#         dp = [float("-inf")] * len(nums)
#         res = float("-inf")

#         for i in range(len(nums)):

                
#             if i == 0:
#                 dp[i] = nums[i]
#             else:
#                 # take the maximum from k units behind 

#                 dp[i] = max(nums[i], nums[i] + max(dp[max(i - k, 0): i]))
                
#             res = max(res, dp[i])
#         return res
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dfs will be TLE because its O(n^2) but lets try it first 
        
        # top down memo 
        
        
        
#         cache = {}
#         def dfs(currentIndex):

#             if currentIndex >= len(nums):
#                 return 0 
            
#             if currentIndex in cache:
#                 return cache[currentIndex]
            
#             temp = nums[currentIndex]
            
#             for i in range(1, k + 1):
#                 temp = max(temp, dfs(currentIndex + i) + nums[currentIndex])

#             cache[currentIndex] = temp

            
#             return cache[currentIndex]
        
        
#         res = float("-inf")
        
#         for i in range(len(nums)):
#             res = max(res, dfs(i))
            
#         return res 