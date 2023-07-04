class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # insert exactly one character
        # delete exactly one character
        # replace one character
        if not s and not t:
            return False
        if abs(len(t) - len(s)) > 1:
            return False
        if s == t:
            return False

        m = len(s)
        n = len(t)
        if m == 0 and n == 1:
            return True
        if m == 1 and n == 0:
            return True
        ptr = 0
        ptr2 = 0
        diff = 0
        while ptr < m and ptr2 < n:
            # print(ptr, ptr2)
            if s[ptr] != t[ptr2]:
                diff += 1
                if m < n: # I need to insert a character
                    ptr2 += 1
                elif m > n: # I need to delete a character
                    ptr += 1

                else: # that means I need to replace a character
                    ptr += 1
                    ptr2 += 1
            else:
                ptr += 1
                ptr2 += 1

        if diff == 0: #
            return (ptr2 == n)  or (ptr == m)
        return diff == 1