class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        # to be removed may contain numbers which are not in the interval
        # first find L
        left = toBeRemoved[0]
        right = toBeRemoved[1]
        res = []
        n = len(intervals)
        # LHS inclusive
        # RHS exclusive
        for i in range(n):
            a, b = intervals[i]
            if a >= left:
                break
            elif b >= left:
                res.append([a, left])
                break

            else:
                res.append([a, b])
        # print(res)
        ptr = i
        while ptr < n:
            a, b = intervals[ptr]
            if a >= right:
                res.append([a, b])
                res = res + intervals[ptr + 1:]
                break
            elif right > a and right < b:
                res.append([right, b])
                res = res + intervals[ptr + 1:]
                break
            else:
                ptr += 1
                # print(res)
        return res





