class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total / 4 != total //4 :
            return False


        goal = total / 4
        n = len(matchsticks)
        @cache
        def dfs(mask, current):
            if mask == 2 **n - 1:
                return True
            can = False
            for i in range(n):
                if (1 << i) & mask == 0:
                    new = mask ^ (1 << i)
                    if current + matchsticks[i] == goal:
                        if dfs(new, 0):
                            return True
                    elif current + matchsticks[i] < goal:
                        if dfs(new, current + matchsticks[i]):
                            return True
            return False
        return dfs(0, 0)