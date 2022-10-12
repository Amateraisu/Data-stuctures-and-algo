class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 :
            return 0 
        if x == 1:
            return 1
        
        
        # basically I want to find the largest num such that num^2 <= x 
        
        res = 0 
        left = 0 
        right = x 
        
        # so what I want to do is that to return the final answer NOT in the while loop 
        
        
        # hence, everytime I find a valid answer, I will assign res to that possible answer 
        # then, move on to find the next best answer, left + 1 BECAUSE the current mid is already the answer 
        
        while left < right:
            mid = left + (right - left)//2 
            if mid**2 > x:
                right = mid
            else:
                res = mid
                left = mid + 1 
                
            
            
        return res