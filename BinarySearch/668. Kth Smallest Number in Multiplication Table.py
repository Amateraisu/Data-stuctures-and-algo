class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        # we need to binary search how many numbers there are

        l = 0
        r = m * n
        res = r
        def valid(mid):
            cur = 0
            for i in range(1, m + 1):
                cur += min(mid//i, n)
            return cur >= k

        while l <= r:
            mid = l + (r - l)//2
            if valid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res