class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        array = [num*-1 for num in nums]
        sum1 = -1 * (sum(array) - kandene(array))
        sum2 = kandene(nums)
        
        
        return max(sum1, sum2)
        
        
def kandene(array):
    res = float("-inf")
    currentTotal = 0
    for i in range(len(array)):
        currentTotal += array[i]
        res = max(currentTotal, res)
        if currentTotal < 0:
            currentTotal = 0 
    return res