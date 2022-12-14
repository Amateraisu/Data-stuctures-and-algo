class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[1], nums[0])
        ptr1 = nums[0]
        ptr2 = max(nums[1], nums[0])
        

        for i in range(2, n):
            # dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            greatest = max(ptr1 + nums[i], ptr2)
            ptr1 = ptr2 
            ptr2 = greatest

        return greatest