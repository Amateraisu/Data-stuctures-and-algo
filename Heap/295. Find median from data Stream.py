class MedianFinder:

    def __init__(self):
        # what we can do is initialise 2 heaps, 
        # 1 min Heap and 1 maxHeap
        # minHeap for the upper 50% values 
        # maxHeap for the lower 50% values 
        self.lenMin = 0 
        self.lenMax = 0 
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        if self.lenMin == self.lenMax:
            heapq.heappush(self.maxHeap, -1 * num)
            self.lenMax += 1
        elif self.lenMax >= self.lenMin:
            heapq.heappush(self.minHeap, num)
            self.lenMin += 1
        # check for balance
        if self.lenMin > 0 and self.lenMax > 0:
            self.updateHeaps()
        # print("added", self.maxHeap, self.minHeap, num)
        return 
    def updateHeaps(self):
        
        rootValueOfMaxHeap = self.maxHeap[0] * -1 
        rootValueOfMinHeap = self.minHeap[0]
        if rootValueOfMaxHeap > rootValueOfMinHeap:
            maxValue = heapq.heappop(self.maxHeap) * -1
            minValue = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, minValue * -1)
            heapq.heappush(self.minHeap, maxValue)
        return 

    def findMedian(self) -> float:
        # check the lengths 

        if self.lenMax > self.lenMin:
            return self.maxHeap[0] * -1 
        elif self.lenMax == self.lenMin:
            maxValue = self.maxHeap[0] * -1 
            minValue = self.minHeap[0] 
            
            return (maxValue + minValue) / 2
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()