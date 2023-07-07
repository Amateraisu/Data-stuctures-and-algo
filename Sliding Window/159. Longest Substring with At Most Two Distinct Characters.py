class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        chars = [0 for i in range(26)]
        chars_upper = [0 for i in range(26)]
        n = len(s)
        l = 0
        res = 0
        c = 0
        for r in range(n):
            char = s[r]
            if char.isupper():
                chars_upper[ord(char.lower()) - ord('a')] += 1
                if chars_upper[ord(char.lower()) - ord('a')] == 1:
                    c += 1
            else:
                chars[ord(char) - ord('a')] += 1
                if chars[ord(char) - ord('a')] == 1:
                    c += 1

            while c > 2:
                if s[l].isupper():
                    chars_upper[ord(s[l].lower()) - ord('a')] -= 1
                    if chars_upper[ord(s[l].lower()) - ord('a')] == 0:
                        c -= 1
                else:
                    chars[ord(s[l]) - ord('a')] -= 1
                    if chars[ord(s[l]) - ord('a')] == 0:
                        c -= 1

                l += 1
            res = max(res, r - l + 1)
        return res
