class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        count = len(set(nums))
        res = []
        cur = set()
        n = len(nums)
        for i in range(n):
            t = len(set(nums[0:i + 1])) - len(set(nums[i + 1:]))
            res.append(t)
        return res