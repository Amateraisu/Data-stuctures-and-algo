class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        ptr1 = 0
        ptr2 = 0
        m = len(source)
        n = len(target)
        one = set(source)
        two = set(target)
        for t in two:
            if t not in one:
                return -1
        res = 0
        while ptr1 < n:
            # try to extend this one as much as possible
            while ptr2 < m and ptr1 < n:
                if target[ptr1] == source[ptr2]:
                    ptr1 += 1

                ptr2 += 1

            res += 1
            ptr2 = 0
        return res

