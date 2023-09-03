class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = collections.defaultdict(int)
        cnt[0] += 1
        cur = 0
        res = 0
        for num in nums:
            cur += num
            cur %= k # my remaindr
            res += cnt[cur]
            cnt[cur] += 1
        return res 