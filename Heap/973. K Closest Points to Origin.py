class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # smallest , so we can do a min Heap
        minHeap = []
        for point in points:
            x, y = point
            distance = sqrt((x**2) + (y**2))
            minHeap.append([distance,x, y])
            
            
            
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            res.append(heapq.heappop(minHeap)[1:])
            k -=1
            
        
        
        

            
        return res