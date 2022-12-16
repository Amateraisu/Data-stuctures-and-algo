from collections import defaultdict
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:


        # so every station is represented as (position, fuel)
        # we want the minimum number of stops to reach the target 
        stations.sort()
        res = 0 
        current = startFuel 
        ptr1 = 0 
        maxHeap = []
        while current < target:
            while ptr1 < len(stations) and stations[ptr1][0] <= current:
                heapq.heappush(maxHeap, -1 * stations[ptr1][1])
                ptr1 += 1 
            # check the maximm of the max heap 
            if not maxHeap: # that means its not possible to reach the end 
                return -1
            maxPossible = heapq.heappop(maxHeap) * -1 
            current += maxPossible 
            res += 1 

        return res  
        # bfs, dfs, 
        # at every position, how do we know if we want to refuel? 
        # so at my current position, if I know I dont have enough gas to reach the target, I will:
        # -  try to get the maximum fuel I can travel in order to reach the goal 
        # -  in that range I can travel, get the maximum amount of gas, 

    def minRefuelStops(self, target, startFuel, s):
        dp = [startFuel] + [0] * len(s)
        for i in range(len(s)):
            for t in range(i + 1)[::-1]:
                if dp[t] >= s[i][0]:
                    dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])
        for t, d in enumerate(dp):
            if d >= target: return t
        return -1