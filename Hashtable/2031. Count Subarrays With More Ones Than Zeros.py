class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        count = collections.defaultdict(int)
        count[0] = 1
        cur = 0
        prev = 0
        res = 0
        for num in nums:
            if num == 1:
                cur += 1
                prev += count[cur - 1]
            else:
                cur -= 1
                prev -= count[cur]
            res = (res + prev) % MOD
            count[cur] += 1

        return res