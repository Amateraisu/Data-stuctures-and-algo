class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def can(target):
            
            timeTaken = 0 
            for pile in piles:
                timeTaken += math.ceil(pile / target)
                
            return timeTaken <= h
        # if h == len(piles), then that means 
        # the slowest case is , 1? 
        left = 1 
        # the least we can is, 
        right = max(piles)
        
        res = right 
        while left <= right :
            mid = left + (right - left)//2 
            
            
            if can(mid):
                res = mid 
                right = mid - 1 
                
            else:
                left = mid + 1 
                
        return res