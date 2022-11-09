class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        numRods = len(rods)
        # shortened to 2 states 
        @cache
        def dp(idx: int, difference: int) -> int:
            nonlocal rods, numRods
            # When we reach the end, if the 2 supports are equal, we return 0
            # else, we return -infinity
            if idx == numRods:
                if difference == 0:
                    
                    return 0
                else:
                    return float("-inf")
            # If we consider rods[idx + 1] for our support
            res1 = rods[idx] + dp(idx + 1, difference + rods[idx])
            # If we consider rods[idx + 1] for the opposite support
            res2 = dp(idx + 1, difference - rods[idx])
            # If we skip rods[idx + 1]
            res3 = dp(idx + 1, difference)
            # Return max of the three conditions because the question
            # asks us to build the tallest billboard
            return max(res1, res2, res3)
        
        return dp(0, 0)
                
                
                
                
                

            
        # TLE because kept track of 2 states 
        
#         total = sum(rods)
        
#         @cache 
#         def dfs(currentIndex, pillar1, pillar2):
#             if currentIndex == len(rods):
#                 # print(pillar1, pillar2)
#                 if pillar1 == pillar2:
#                     return pillar1
#                 else:
#                     return float("-inf")
                
#             best = max(dfs(currentIndex + 1, pillar1 + rods[currentIndex], pillar2), dfs(currentIndex + 1, pillar1, pillar2 + rods[currentIndex]), dfs(currentIndex + 1, pillar1, pillar2))
            
            
            
#             return best 
        
        
#         res = dfs(0, 0, 0)
        
#         return res