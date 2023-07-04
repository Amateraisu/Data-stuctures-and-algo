class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr1 = 0
        ptr2 = len(s) - 1
        while ptr1 < ptr2:
            s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
            ptr1 += 1
            ptr2 -= 1
        print(s)
        prev = 0
        for i in range(len(s)):
            if s[i] == ' ':
                # reverse the words
                ptr1 = prev
                ptr2 = i - 1
                while ptr1 < ptr2:
                    s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                    ptr1 += 1
                    ptr2 -= 1
                prev = i + 1
        ptr1 = prev
        ptr2 = len(s) - 1
        while ptr1 < ptr2:
            s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
            ptr1 += 1
            ptr2 -= 1
        prev = i + 1

        return s