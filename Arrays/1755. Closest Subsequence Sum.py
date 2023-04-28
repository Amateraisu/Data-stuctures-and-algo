class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)

        mid = n//2
        left = nums[:mid]
        leftList = []
        right = nums[mid:]
        rightList = []

        def generateSubset(currentList, curIndex, current, l):
            if curIndex == len(l):
                currentList.append(sum(current))

                return


            new = current + [l[curIndex]]
            generateSubset(currentList, curIndex + 1, new, l)
            generateSubset(currentList, curIndex + 1, current, l)
            return

        generateSubset(leftList, 0, [], left)
        generateSubset(rightList, 0, [], right)
        leftList.sort()
        rightList.sort()
        res = float('inf')

        for num in leftList:
            complement = goal - num
            idx = bisect.bisect_left(rightList, complement)

            for i in [idx - 1, idx, idx + 1]:
                if 0 <= i < len(rightList):
                    total = rightList[i] + num
                    res = min(res, abs(goal - total))

        return res