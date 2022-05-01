class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTimes = []
        endTimes = []
        res = 0
        for interval in intervals:
            startTimes.append(interval[0])
            endTimes.append(interval[1])
        startTimes.sort()
        endTimes.sort()
        ptr1 = 0 
        ptr2 = 0 
        count = 0 
        res = 0 
        while ptr2 < len(endTimes):

            
            if ptr1 < len(startTimes) and startTimes[ptr1]< endTimes[ptr2]:
                ptr1 += 1 
                count += 1
            else:
                ptr2+=1
                count-=1
            res = max(res, count)
            
            
        return res