class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.KthLargest = k
        self.elements = nums

    def add(self, val: int) -> int:
        self.elements.append(val)
        self.elements.sort()
        count = self.KthLargest
        
        length = len(self.elements)
        while count != 0:
            length -= 1
            count-=1
            

        return self.elements[length]