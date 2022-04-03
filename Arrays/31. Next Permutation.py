class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        ptr2 = len(nums)-1
        ptr1 = 0
        while nums[ptr2-1] >= nums[ptr2] and ptr2>0:
            ptr2 -=1
        
        
        # so if the whole sequence is decreasing, 
        # check here 
        ptr1 = ptr2 - 1
        if ptr1 < 0:
            # just reverse the whole array here 
            ptr1 = 0
            ptr2 = len(nums)-1
            while ptr1<ptr2:
                nums[ptr1] , nums[ptr2] = nums[ptr2] , nums[ptr1]
                ptr1+=1
                ptr2-=1
            
        else:
            # longestStrictlyDecreasing = nums[ptr2:len(nums)+1]
            # longestStrictlyDecreasing = 
            ptr3 = ptr2 #ptr3 is at the first index of the strictly decreasing subsequence 
            ptr2 = len(nums)-1
     
        
            while nums[ptr2] <= nums[ptr1] and ptr2>ptr3:
                ptr2-=1
            
            #swap the 2 numbers here 
            nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
            ptr1 = ptr3
            ptr2 = len(nums)-1
            
            #sort here 
            while ptr1 < ptr2:
                nums[ptr1] , nums[ptr2] = nums[ptr2] , nums[ptr1]
                ptr1+=1
                ptr2-=1
            
            
            
        return nums