class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTimes = sorted([interval[0] for interval in intervals])
        endTimes = sorted([interval[1] for interval in intervals])
        # print(startTimes, endTimes)
        res = 0 
        room = 0 
        # everytime my startTime increments, room += 1 
        # everytime my endTime increments, room -= 1
        i = 0 
        j = 0 
        while i < len(intervals) and j < len(intervals):
            start = startTimes[i]
            end = endTimes[j]
            if start < end:
                room += 1 
                i += 1 
            if end < start:
                room -= 1 
                j += 1 
            if end == start:
                i += 1 
                j += 1 
            res = max(room , res)
            
        return res