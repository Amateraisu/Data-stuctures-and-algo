class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        dp = collections.defaultdict(int)
        for i, student in enumerate(students):
            for j, men in enumerate(mentors):
                score = calc(student, men)
                dp[(i, j)] = score


        n = len(students)
        @cache
        def dfs(index, m):
            if index == n:
                return 0
            best = float('-inf')
            for i in range(n):
                if (1 << i) & m == 0:
                    new = (1 << i) ^ m
                    best = max(best, dp[(index, i)] + dfs(index + 1, new))
            return best
        return dfs(0, 0)

def calc(student, men):
    res = 0
    for i in range(len(student)):
        if student[i] == men[i]:
            res += 1
    return res