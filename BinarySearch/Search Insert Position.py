class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # assume I will find the minimum position bah 
        # so I will find a minimum position at index i where nums[i] <= target
        
        left = 0 
        right = len(nums) - 1 
        
        while left <= right:
            mid = left + (right - left)//2 
            
            if nums[mid] < target:
                left = mid + 1 
            else:
                right = mid - 1 
            print(left, right)
            
        return left