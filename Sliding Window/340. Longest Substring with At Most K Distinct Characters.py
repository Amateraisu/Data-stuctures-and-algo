class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        chars = collections.defaultdict(int)
        l = 0
        n = len(s)
        res = 0
        for r in range(n):
            chars[s[r]] += 1
            while len(chars) > k:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
