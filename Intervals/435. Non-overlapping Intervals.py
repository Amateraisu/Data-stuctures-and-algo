class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0 
        res = 0
        intervals.sort(key = lambda x : x[0])
        
        prevEnd = intervals[0][1]
        
        for i in range(1, len(intervals)):
            currentStart, currentEnd = intervals[i]
            
            if currentStart < prevEnd: # if intersect
                res += 1 
                prevEnd = min(prevEnd, currentEnd)
            else:
                prevEnd = currentEnd
                
        return res