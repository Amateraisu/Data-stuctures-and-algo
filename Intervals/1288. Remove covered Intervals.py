class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        new_intervals = sorted(intervals , key = lambda x : (x[0], -x[1]))
        print(new_intervals)
        stack = []
        
        for interval in new_intervals:
            if stack and stack[-1][0] <= interval[0] and interval[1] <= stack[-1][1]:
                continue 
            else:
                stack.append(interval)

        return len(stack)