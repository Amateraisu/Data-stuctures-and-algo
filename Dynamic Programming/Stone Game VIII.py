class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # choose an integer x > 1 
        # remove the leftmost x stones from the row 
        
        # add the sum of the removed stones to the player's score 
        # place a new sum, on the left side of the row 
        
        
        # FIND the score difference if they both play optimally 
        N = len(stones)
        inf = 10 ** 10 
        
        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1] + x)
            
        @cache
        
        # what is the maximum "score" starting on this index 
        
        
        def go(index):
            if index == N:
                return 0 
            best = -inf
            
            # you take the stone 
            score = go(index + 1) + stones[index]
            best = max(score, best)
            
            # let the opponent take 
            score = -(go(index + 1) + prefix[index + 1])
            
            best = max(score, best)
            
            return best
        
        return go(2) + stones[0] + stones[1]