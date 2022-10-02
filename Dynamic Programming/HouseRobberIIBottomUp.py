class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1 = solveRob(nums[0:-1])
        rob2 = solveRob(nums[1:])
        
        
        

        return max(rob1, rob2)
    
    
    
    
def solveRob(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums)
    dp = [0 for num in nums]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i] , dp[i - 1])

    return dp[-1]