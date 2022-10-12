class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        # find the minimum sum to split the subarray 
        # so if we find a sum in which we cannot split a sum upon, change accordingly 
        # if we can, set res = mid 
        # then, left = mid + 1 
        
        def canSplit(mid):
            count = 1 
            total = 0 
            for num in nums:
                total += num 
                if total > mid:
                    count += 1 
                    total = num 
                    
            return count <= m
        
        res = right
        while left <= right:
            mid = left + (right - left)//2
            
            if canSplit(mid):
                res = mid 
                # then find the minimum range, so change the right ptr 
                right = mid - 1 
            else:
                left = mid + 1 
                
        return res 