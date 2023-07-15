class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [start for start, e, v in events]

        @cache
        def dfs(curIndex, cur):
            if curIndex == len(events) or cur == k:
                return 0

            i = bisect.bisect_right(starts, events[curIndex][1])
            res = max(dfs(curIndex + 1, cur), events[curIndex][2] + dfs(i, cur + 1))
            return res

        return dfs(0, 0)