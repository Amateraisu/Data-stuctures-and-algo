class Solution:
    def solve(self, nums, k):
        # basically find the largest prefix that does not exceed k 
        current = 0 
        res = -1
        for i in range(len(nums)):
            current += nums[i]
            if current <= k:
                res = i 

        return res 