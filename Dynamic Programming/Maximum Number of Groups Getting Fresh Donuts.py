class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        ng = [0] * batchSize # 
        for g in groups:
            ng[g% batchSize] += 1 
        ngt = tuple(ng)
        print(ngt)
        
        @cache
        def go(current, offset):
            best = 0 
            
            ng = list(current)
            for x, c in enumerate(current):
                if c == 0:
                    continue 
                    
                if offset == 0:
                    ng[x] = c - 1
                    best = max(best, go(tuple(ng), (x + offset) % batchSize) + 1)
                    ng[x] = c
                else:
                    ng[x] = c - 1 
                    best = max(best, go(tuple(ng), (x + offset) % batchSize))
                    ng[x] = c 
            return best
        
        return go(ngt, 0)