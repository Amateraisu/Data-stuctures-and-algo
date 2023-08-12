class Solution:
    def uniquePathsIII(self, g: List[List[int]]) -> int:
        end = (0, 0)
        start = (0, 0)
        m = len(g)
        n = len(g[0])
        goal = m * n
        for i in range(m):
            for j in range(n):
                if g[i][j] == 2:
                    end = (i, j)
                elif g[i][j] == -1:
                    goal -= 1
                elif g[i][j] == 1:
                    start = (i, j)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        res = 0
        visited.add((start[0], start[1]))
        def dfs(r, c):
            nonlocal res
            if (r, c) == end:
                if len(visited) == goal:
                    res += 1
                return
            for d in directions:
                nx = r + d[0]
                ny = c + d[1]
                if nx >= 0 and nx < m and ny >= 0 and ny < n and g[r][c] != -1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dfs(nx, ny)
                    visited.discard((nx, ny))
            return

        dfs(start[0], start[1])
        return res