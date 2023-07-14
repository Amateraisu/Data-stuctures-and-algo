class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        words = set(words)
        if not words:
            return s
        n = len(s)
        intervals = []
        for i in range(n):
            c = ""
            for j in range(i, n):
                c += s[j]
                if c in words:
                    intervals.append([i, j])
        # print(intervals)
        if not intervals:
            return s
        res = [intervals[0]]
        m = len(intervals)
        for i in range(1, m):
            a, b = intervals[i]
            prev = res[-1][1]
            if prev + 1 >= a:
                res[-1][1] = max(res[-1][1], b)
            else:
                res.append([a, b])
        ret = ""
        # print(res)
        # print(s[0:0], "test")
        prev = 0
        for a, b in res:
            ret += s[prev:a]
            ret += "<b>"
            ret += s[a:b + 1]
            ret += "</b>"
            prev = b + 1
        ret += s[prev:n]

        return ret