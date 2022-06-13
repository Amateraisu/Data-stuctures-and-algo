class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # wall = -1 
        # gate = 0 
        # 2147483647 = empty room 
        
        queue = deque()
        
        num_rows , num_cols = len(rooms), len(rooms[0])
        
        for i in range(num_rows):
            for j in range(num_cols):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        def bfs(queue):
            if len(queue) == 0:
                return 
            distance = 1 
            while queue:
                numberOfNodes = len(queue)
                for i in range(numberOfNodes):
                    row, col = queue.popleft()
                    if row - 1 >=0 and rooms[row-1][col] > rooms[row][col]:
                        queue.append((row-1, col))
                        rooms[row-1][col] = distance 
                    if row + 1 < num_rows and rooms[row + 1][col] > rooms[row][col]:
                        queue.append((row + 1, col))
                        rooms[row+1][col] = distance 
                    
                    if col - 1 >=0 and rooms[row][col - 1] > rooms[row][col]:
                        queue.append((row, col - 1))
                        rooms[row][col - 1] = distance 
                    if col + 1 < num_cols and rooms[row][col + 1] > rooms[row][col]:
                        queue.append((row, col + 1))
                        rooms[row][col + 1] = distance
                        
                distance += 1 
            return 
        bfs(queue)
        return rooms