class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap , self.k = nums, k
        heapq.heapify(self.minHeap) #O(n) opeartion
        while len(self.minHeap) > k :
            heapq.heappop(self.minHeap) #O(logn) operation
            

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


#I can use a min Heap to do this
# min heap of size K 
# add / pop will be in logn Time
# access to min will be O(1) time 