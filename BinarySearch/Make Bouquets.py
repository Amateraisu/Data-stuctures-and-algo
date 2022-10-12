class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        
        
        def canMake(target):
            # 
            current = 0 
            bouquetsMade = 0 
            for day in bloomDay:
                if day > target:
                    current = 0 
                elif day <= target:
                    current+= 1 
                if current == k:
                    bouquetsMade += 1 
                    current = 0 
            # print("target", m, "current", bouquetsMade, "day", target)
            return bouquetsMade >= m

        
        res = -1 
        
        left = min(bloomDay)
        right = max(bloomDay)
        
        
        while left <= right:
            mid = left + (right - left)//2 
            
            
            if canMake(mid):
                res = mid 
                
                right = mid - 1 
            else:
                left = mid + 1 
            print(left, right, res, mid)
                
        return res