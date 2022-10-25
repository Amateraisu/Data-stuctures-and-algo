class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        left = -1 
        zero_index = -1 
        res = float("-inf")
        for i in range(len(nums)):
            cur = nums[i]
            if cur == 0:
                res = max(res, i - left - 1)
                left = zero_index + 1 
                zero_index = i 


        return max(res, i - left )