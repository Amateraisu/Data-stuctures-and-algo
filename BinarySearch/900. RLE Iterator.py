from collections import Counter
class RLEIterator:

    def __init__(self, encoding: List[int]):
        # [3, 8, 0, 9, 2, 5]
        self.currentSum = 0
        self.processed = []
        self.mapper = {}
        
        for i, num in enumerate(encoding):
            if i % 2 == 0 and num != 0:
                self.processed.append(num)
            elif len(self.processed) - 1 not in self.mapper:
                self.mapper[len(self.processed) - 1] = num 

        # create a prefix sum too 
        self.prefixSum = [0] * len(self.processed)
        curr = 0 
        for j in range(len(self.processed)):
            curr += self.processed[j]
            self.prefixSum[j] = curr


    def next(self, n: int) -> int:
        # do a binary search on the prefixSum to find the current proper count 
        self.currentSum += n 
        # binary search on the prefix Sum 
        if self.currentSum > self.prefixSum[-1]:
            return -1 
        left = 0 
        right = len(self.prefixSum) - 1

        resIndex = right


        while left <= right:
            mid = left + (right - left)// 2 
            if self.currentSum <= self.prefixSum[mid]:
                resIndex = mid 
                right = mid - 1  
            else:
                left = mid + 1
        

        
        return self.mapper[resIndex]



# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)