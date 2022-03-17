class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        
        
        currentMax = 1
        currentMin = 1
        
        for index in range(0,len(nums)):
            if nums[index] == 0:
                currentMax = 1
                currentMin = 1
                continue
            temp = currentMax * nums[index]
            currentMax = max(nums[index], currentMax * nums[index], currentMin*nums[index])
            
            currentMin = min(temp, currentMin*nums[index], nums[index])
            result = max(currentMax, result)
            
            
        return result
                