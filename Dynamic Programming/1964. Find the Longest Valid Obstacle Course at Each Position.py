from sortedcontainers import SortedList


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # isnt this just longest increasing subsequence?
        n = len(obstacles)
        dp = []
        res = []
        for num in obstacles:
            # print(num, dp)
            i = bisect_right(dp, num)
            # print(i, num)
            if i == len(dp):
                dp.append(num)
                res.append(i + 1)
            else:  # that means the number is smaller
                res.append(i + 1)
                dp[i] = num
            # print(dp, res)
        return res

5 0
1 0
5 1
5 2
1 1
3 2
4 3
5 4
1 2
4 4