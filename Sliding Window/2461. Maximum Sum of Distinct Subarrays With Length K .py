from collections import Counter

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0 
        # print(nums)
        myMap = Counter(nums)
        # shift all 0s to the end 
        zeros = 0 
        for num in nums:
            if num == 0:
                zeros += 1 
                
        res = []
        for j in range(0, len(nums)):
            if nums[j] != 0:
                res.append(nums[j])
                
        res = res + [0] * zeros
            
        return res