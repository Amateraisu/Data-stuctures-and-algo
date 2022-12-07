class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        print(timePoints)
        res = float("inf")
        for i in range(1, len(timePoints)):
            difference = getDiff(timePoints[i], timePoints[i - 1])
            res = min(res, difference)

        # get the diff between the first and the last element, counting backwards
        # get the difference between the last element and the 00:00, then count the difference between the first element and the last 
        cost = getDiff0(timePoints[-1])
        cost2 = getDiff(timePoints[0], "00:00")

        res = min(res, cost + cost2)
        return res
def getDiff0(time):
    minutesDiff = 60 - (int(time[3:5]))
    currentHour = int(time[:2]) + 1
    hourDiff = 24 - currentHour

    return hourDiff * 60 + minutesDiff



def getDiff(time1, time2):
    minutesDiff = int(time1[3:5]) - int(time2[3:5])
    hoursDiff = int(time1[:2]) - int(time2[:2])
    totalDiff = minutesDiff + hoursDiff * 60

    return totalDiff