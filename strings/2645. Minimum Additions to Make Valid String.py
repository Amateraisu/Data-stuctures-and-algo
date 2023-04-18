class Solution:
    def addMinimum(self, word: str) -> int:
        # it comes in sets
        res = 0
        # so every a must come before every b, and every c must come before every
        n = len(word)
        seen = set()
        stack = []

        ptr1 = 0
        while ptr1 < n:
            starting = word[ptr1]
            seen = set()
            seen.add(starting)
            temp = ptr1 + 1
            prev = starting
            while temp < n and word[temp] > prev:
                prev = word[temp]
                temp += 1

                # once I see a repeat, add the missing numbers
            res += 3 - (temp - ptr1)
            ptr1 = temp

        return res






