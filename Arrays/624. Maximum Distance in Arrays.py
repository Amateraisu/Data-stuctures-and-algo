class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini = float('inf')
        maxi = float('-inf')
        res = float('-inf')
        for arr in arrays:
            res = max(res, maxi - arr[0])
            res = max(res, arr[-1] - mini)
            maxi = max(maxi, arr[-1])
            mini = min(mini, arr[0])
        return res