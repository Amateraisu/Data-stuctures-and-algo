class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # I should delete one element from it
        res = 0
        l = 0
        n = len(nums)
        c = 0
        for r in range(n):
            if nums[r] == 0:
                c += 1
            while c > 1 and l < r:
                if nums[l] == 0:
                    c -= 1
                l += 1
            res = max(res, r - l)
        return res