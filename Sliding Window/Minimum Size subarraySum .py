class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        currentSum = 0 
        res = float("inf")
        for right, num in enumerate(nums):
            currentSum += num
            while currentSum >= target:
                res = min(res, right - left + 1)
                
                currentSum -= nums[left]
                left += 1
                
                
                
                
                
                
        return res if res != float("inf") else 0