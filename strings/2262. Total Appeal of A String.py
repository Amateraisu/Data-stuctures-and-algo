class Solution:
    def appealSum(self, s: str) -> int:
        last = defaultdict(lambda: -1)
        res, n = 0, len(s)
        for i, c in enumerate(s):
            res += (i - last[c]) * (n - i)
            last[c] = i
        return res