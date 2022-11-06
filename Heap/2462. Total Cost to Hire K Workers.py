class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # add the first k and last k candidates to my minheap 
        
        minHeap = []
        N = len(costs)
        seenIndex = set()
        for i in range(N):
            toAdd = [costs[i], i]
            if i <= candidates - 1 or i >= N  - candidates:
                heapq.heappush(minHeap, toAdd)
                seenIndex.add(i)
                
                
        # keep track of ptrs on the left and right side 
        left = candidates - 1 
        right = N - candidates 
        
                
        res = 0 
        while k > 0:
            # hire a candidate with the lowest index
            
            cost, index = heapq.heappop(minHeap)
            if index <= left and left < right and left + 1 not in seenIndex:
                left += 1 
                heapq.heappush(minHeap, [costs[left], left])
                seenIndex.add(left)
            elif index >= right and left < right and right - 1 not in seenIndex:
                right -= 1 
                heapq.heappush(minHeap, [costs[right], right])
                seenIndex.add(right)
            
            
            res += cost
            k -= 1 
            
            
        return res 