class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        events = []
        for i in range(n):
            # 1 for start event
            # 0 for end event
            # We want end events to occur before start event for same time
            events.append((startTime[i], "start", i))
            events.append((endTime[i], "end", i))
            
        events.sort()
        print(events)
        
        maxProfit = [0]*n
        previousMax = 0
        
        for time, eventType, index in events:
			# If it is a start event, calculate its maximum profit, using previous maximum profit
            if eventType == "start":
                maxProfit[index] = previousMax + profit[index]
			# If it is an end, update previous maximum profit
            else:
                previousMax = max(maxProfit[index], previousMax)
            
        return previousMax
        
        
# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        
#         intervals = []
        
#         for i in range(len(startTime)):
#             start, end , p = startTime[i], endTime[i], profit[i]
            
#             intervals.append([start, end, p])
            
            
#         intervals.sort()

#         @cache
#         def dfs(currentIndex):
#             if currentIndex >= len(intervals):
#                 return 0 
            

#             start, end , p = intervals[currentIndex]
            
#             nextIndex = binary(currentIndex, end, intervals)



#             best = max(
#                 dfs(currentIndex + 1),
#                 dfs(nextIndex) + p
#             )

#             return best 
        
#         return dfs(0)
        
        
# def binary(left, end, intervals):

#     left = left + 1

#     right = len(intervals) - 1
#     res = len(intervals)

#     while left <= right:
#         mid = left + (right - left)//2 
        
#         if intervals[mid][0] >= end:
#             res = mid 
#             right = mid - 1 
#         else:
#             left = mid + 1 

#     return res 