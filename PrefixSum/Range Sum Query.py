class NumArray:

    def __init__(self, nums: List[int]):
        self.cache = [0] * (len(nums) + 1 )
        res = 0 
        for index, num in enumerate(nums):
            self.cache[index] = res 
            res += num 
        self.cache[-1] = res
            
            

    def sumRange(self, left: int, right: int) -> int:
        return self.cache[right + 1] - self.cache[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)