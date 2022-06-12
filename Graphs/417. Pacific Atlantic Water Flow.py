class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            # O(2 m*n) since we are not doing repeated work on every single node.
            return []
        
        num_rows , num_cols = len(matrix), len(matrix[0])
        
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(num_rows):
            pacific_queue.append((i,0))
            atlantic_queue.append((i, num_cols - 1))
        for i in range(num_cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((num_rows - 1, i))
        # print(pacific_queue, atlantic_queue)
        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                reachable.add((row, col))
                if row + 1 < num_rows and (row+1, col) not in reachable and matrix[row][col] <= matrix[row + 1][col]:
                    queue.append((row+ 1, col))
                    
                if row - 1 >= 0 and (row-1 , col) not in reachable and matrix[row][col] <= matrix[row - 1][col]:
                    queue.append((row - 1, col))
                    
                if col - 1 >= 0 and (row, col - 1) not in reachable and matrix[row][col] <= matrix[row][col - 1]:
                    queue.append((row, col - 1))
                    
                if col + 1 < num_cols and (row, col + 1) not in reachable and matrix[row][col] <= matrix[row][col + 1]:
                    queue.append((row, col + 1))
            
            print(reachable)    
            return reachable
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        return list(pacific_reachable.intersection(atlantic_reachable))