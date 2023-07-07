class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        a = 0
        b = 0
        l = 0
        n = len(nums)
        res = 0
        for r in range(n):
            if nums[r] == 1:
                a += 1
            else:
                b += 1
            while b > k:
                if nums[l] == 1:
                    a -= 1
                else:
                    b -= 1
                l += 1
            res = max(res, a + b)

        return res
