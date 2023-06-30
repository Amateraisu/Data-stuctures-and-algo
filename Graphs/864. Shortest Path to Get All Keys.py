class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        c = 0
        start = [-1, -1]
        all_keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j].isalpha() and grid[i][j].islower():
                    c += 1
                    all_keys += (1 << (ord(grid[i][j]) - ord('a')))
                if grid[i][j] == '@':
                    start = [i, j]
        if start == [-1, -1]:
            return -1

        visited = set()
        q = collections.deque()
        mask = 0
        q.append([start[0], start[1], mask, 0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited.add((start[0], start[1], mask))
        # print(mask, end)
        # print(c)
        res = float('inf')
        while q:
            # print(q)
            r, c, mask, moves = q.popleft()
            if mask == all_keys:
                res = min(res, moves)
                continue
            for direct in directions:
                nr = r + direct[0]
                nc = c + direct[1]
                if nr >= 0 and nr <= m - 1 and nc >= 0 and nc <= n - 1 and grid[nr][nc] != '#':
                    new = mask
                    # print("CELL")

                    if grid[nr][nc].isalpha() and grid[nr][nc].islower():  # it is a key
                        # print("key")
                        keyNumber = ord(grid[nr][nc]) - ord('a')
                        new = (mask | (1 << (ord(grid[nr][nc]) - ord('a'))))  # get a new key
                        if (nr, nc, new) not in visited:
                            visited.add((nr, nc, new))
                            q.append((nr, nc, new, moves + 1))



                    elif grid[nr][nc].isalpha() and grid[nr][nc].isupper():  # it is a lock
                        # print('lock', (1 << keyNumber) & mask)
                        # check if we have a lock
                        keyNumber = ord(grid[nr][nc].lower()) - ord('a')
                        if (1 << keyNumber) & mask and (nr, nc, new) not in visited:  # we have the corresponding key
                            visited.add((nr, nc, new))
                            q.append((nr, nc, new, moves + 1))

                    else:  # it is an empty space
                        # print('empty')
                        if (nr, nc, new) not in visited:
                            visited.add((nr, nc, new))
                            q.append((nr, nc, new, moves + 1))

            # print(q, 'end')

        return res if res != float('inf') else -1