class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we can do this using a heap. 
        # heapify will be O(n) time complexity 
        # popping from heap will be O(logn) time complexity
        # for every smash, it will be O(3logn) time complexity which will be transformed into O(logn) time complexity 
        # worse case will be both stones will not always be destroyed. 
        # hence time complexity will be O(nlogn) while a space complexity of O(n) fin order to establish our heap
        
        # since we want a max heap, 
        # we can change the stones to be negative, 
        
        for index in range(len(stones)):
            stones[index] = -1 * stones[index]
        heapq.heapify(stones)
        # this will then be a max heap 
        # remember to multiply by -1 for each value 
        while len(stones) > 1:
            firstStone = heapq.heappop(stones)
            if firstStone < 0:
                firstStone *= -1
            secondStone = heapq.heappop(stones)
            if secondStone < 0:
                secondStone *= -1
            absoluteDiff = abs(firstStone - secondStone)
            if absoluteDiff > 0:
                heapq.heappush(stones, -1 * absoluteDiff)
                
            
        return abs(stones[0]) if len(stones) > 0 else 0