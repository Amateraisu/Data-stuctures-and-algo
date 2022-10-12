class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights) 
        right = sum(weights)
        res = 0
        
        while left <= right:
            mid = left + (right - left)//2 
            
            
            if self.canSplit(mid, weights, days):
                res = mid
                right = mid - 1 
            else:
                left = mid + 1
            
            
        return res 
    
    
    def canSplit(self, weightToSplit, weights, days):
        count = 1 
        currentTotal = 0 
        for weight in weights:
            currentTotal += weight 
            if currentTotal > weightToSplit:
                currentTotal = weight 
                count += 1 
        return count <= days