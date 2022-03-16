class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n) time complexity  | O(1) Space complexity 
        if len(nums) == 1:
            return nums[0]
        
        
        ptr1 = 0
        ptr2 = 0
        total = nums[ptr1]
        maximum = total
        
        while ptr2<len(nums)-1:
            ptr2+=1
            if total < 0 and nums[ptr2]>total:
                ptr1 = ptr2
                total = nums[ptr1]
            else:
                total += nums[ptr2]
            
            if total > maximum:
                maximum = total
        
        return maximum