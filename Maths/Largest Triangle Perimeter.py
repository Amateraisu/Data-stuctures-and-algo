class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # basically the 3 largest length.
        # the sum of all internal angles is 180 
        # the length of any side of the rectangle is shorter than the sum of 2 other sides 
        nums.sort()
        # from the last number, get 
        
        
        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                return nums[i] + nums[i - 1] + nums[i - 2]
            
        return 0