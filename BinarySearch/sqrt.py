class Solution:
    def mySqrt(self, x: int) -> int:
        # we can do binary Search here 
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 0 
        right = x
        # we are finding the maximal k such that k**2 >= x 
        
        # 0 ** 2 = 0 
        # left = 1 
        while left < right:
            mid = left + (right - left)//2 
            
            if mid**2 > x:
                right = mid  
            elif mid**2 < x:
                left = mid + 1
                
            else:
                return mid 
            
        return left - 1