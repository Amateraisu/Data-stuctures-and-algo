class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        # count the number of zeros in between every pair of zeros
        c = 0
        ones = []
        res = 1
        for i, num in enumerate(nums):
            if num == 1:
                c += 1
                ones.append(i)
        mod = 10 ** 9 + 7

        if c == 1:
            return 1
        if c == 0:
            return 0
        for i in range(1, len(ones)):
            res *= ones[i] - ones[i - 1]
        return res % mod