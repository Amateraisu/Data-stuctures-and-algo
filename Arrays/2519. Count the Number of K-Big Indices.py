from sortedcontainers import SortedList


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = [False for i in range(n)]
        r = [False for i in range(n)]

        res = 0
        # print(l)
        # print(r)
        t = SortedList()
        for i, num in enumerate(nums):
            if t.bisect_left(num) >= k:
                l[i] = True
            t.add(num)

        t = SortedList()
        for j in range(n - 1, -1, -1):
            num = nums[j]

            if t.bisect_left(num) >= k:
                r[j] = True
            t.add(num)
        #     print(t)
        # print(l)
        # print(r)
        for i in range(n):
            if l[i] and r[i]:
                res += 1

        return res

