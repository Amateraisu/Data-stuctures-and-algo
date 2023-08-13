from sortedcontainers import SortedList


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        myList = SortedList()
        n = len(nums)
        res = float('inf')
        for i, num in enumerate(nums):
            myList.add(num)
            if i + x < n:
                l = myList.bisect_left(nums[i + x])
                if l == len(myList):
                    res = min(res, abs(nums[i + x] - myList[l - 1]))
                else:
                    res = res = min(res, abs(nums[i + x] - myList[l - 1]), abs(nums[i + x] - myList[l]))

        return res