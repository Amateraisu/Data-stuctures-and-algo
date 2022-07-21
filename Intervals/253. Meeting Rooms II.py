class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x[0])
        
        res = 1
        heap = []
        heap.append(intervals[0][1])
        for index in range(1, len(intervals)):
            currentInterval = intervals[index]
            currentStart, currentEnd = currentInterval
            # print(heap)
            while heap and currentStart >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, currentEnd)
            res = max(res, len(heap))
            
        return res