class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        # O(n) solution 
        
        decreasingStack = []
        increasingStack = []
        
        res = 0 
        for i in range(len(nums) + 1):
            currentNum = nums[i] if i <= len(nums) - 1 else -1
            
            # increasing stack to find the minimum of ranges 
            while increasingStack and (i == len(nums) or currentNum <= nums[increasingStack[-1]]):
                mid = increasingStack.pop()
                
                right = i 
                left = increasingStack[-1] if increasingStack else -1 
                count = (right - mid) * (mid - left)
                res -= count * nums[mid]
                
            # decreasingStack to find the maximum of ranges 
            while decreasingStack and (i == len(nums) or currentNum >= nums[decreasingStack[-1]]):
                mid = decreasingStack.pop()
                right = i 
                left = decreasingStack[-1] if decreasingStack else -1
                count = (right - mid) * (mid - left)
                res += count * nums[mid]
            decreasingStack.append(i)
            increasingStack.append(i)
        return res 
        
        
        
        # O(n^2)

#         res = 0 
#         for i in range(len(nums)):
#             currentMaxi = float("-inf")
#             currentMini = float("inf")
#             for j in range(i, len(nums)):
#                 currentMaxi = max(currentMaxi, nums[j])
#                 currentMini = min(currentMini, nums[j])
                
#                 res += currentMaxi 
#                 res -= currentMini
            
#         return res 