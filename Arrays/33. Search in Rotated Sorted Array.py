class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # so i need to binary search the smallest number first. 
        # then do a normal binary search to find the target 
        
        
        left = 0 
        right = len(nums)-1

        while left<right:

            middle = int(left + (right - left)/2)

            if nums[right] >= nums[middle]: #this is normal. look on the left then.
                right = middle

            else:

                left = middle +1

        
        start = left
    
        left = 0 
        right = len(nums)-1
        if target >= nums[start] and target <= nums[right]:
            left =  start
        else:
            right = start-1
            
        while left <= right :
        
            middle = round(left + (right-left)/2)
            #element found 
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle-1
        
            
        return -1
        