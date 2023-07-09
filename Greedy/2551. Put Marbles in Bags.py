class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        n = len(weights)
        pairs = [0] * (n - 1)
        for i in range(n - 1):
            pairs[i] = weights[i] + weights[i + 1]
        pairs.sort()
        res = 0
        for i in range(k - 1):
            res += pairs[n - 2 - i] - pairs[i]
        return res