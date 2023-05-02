class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        pref = []
        c = 0
        for num in nums:
            pref.append(c)
            c += num
        pref.append(c)
        stack = []
        res = 0
        for i, num in enumerate(nums):
            start = i
            while stack and stack[-1][1] > num:
                curStart, curHeight = stack.pop()
                res = max(res, curHeight * (pref[i] - pref[curStart]))

                start = curStart
            stack.append([start, num])
        for ele in stack:
            res = max(res, ele[1] * (pref[-1] - pref[ele[0]]))
        return res % MOD