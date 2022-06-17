class Solution:
    def rob(self, nums: List[int]) -> int:
        # O(n) time and O(n) space 
        if len(nums) <= 2:
            return max(nums)
#         dp = [0 for i in range(len(nums))]
        
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])
        
#         for i in range(2, len(nums)):
#             dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            

#         return dp[-1]
# O(n) time and O(1) space
        ptr1 = nums[0]
        ptr2 = max(nums[0], nums[1])
        res = 0
        for i in range(2, len(nums)):
            res = max(nums[i] + ptr1, ptr2)
            temp = ptr2 
            ptr1 = ptr2 
            ptr2 = res 
        return res