class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        left = 0
        c = 0
        res = 0
        n = len(s)
        for right in range(n):
            while right - left + 1 > k:
                if s[left] in vowels:
                    c -= 1
                left+= 1
            if s[right] in vowels:
                c += 1
            res = max(res, c)

        return res