class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        l = [int(x%modulo==k) for x in nums]
        ret = 0
        cur = 0
        d = collections.defaultdict(int)
        d[0] = 1
        for x in l:
            cur += x
            cur %= modulo
            ret += d[(cur - k) % modulo]
            d[cur] =  d[cur] + 1
        return ret