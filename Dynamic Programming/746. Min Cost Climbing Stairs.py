class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # O(n) time | O(n) space
        stairArray = [0 for index in range(len(cost)+1)]
        
        stairArray[0] = 0
        stairArray[1] = 0
        
        for stairNum in range(2, len(stairArray)):
            stairArray[stairNum] = min(cost[stairNum-1] + stairArray[stairNum-1],cost[stairNum-2] + stairArray[stairNum-2])
            
            
        return stairArray[-1]