class Solution:
    def dfs(self, nums, index, dp):
        if index == len(nums):
            return True
        if dp[index] != -1:
            return dp[index]

        can1, can2, can3 = False, False, False
        if index + 1 < len(nums) and nums[index] == nums[index + 1]:
            can1 = self.dfs(nums, index + 2, dp)
        if index + 2 < len(nums) and nums[index] == nums[index + 1] and nums[index + 1] == nums[index + 2]:
            can2 = self.dfs(nums, index + 3, dp)
        if index + 2 < len(nums) and nums[index] == nums[index + 1] - 1 and nums[index] == nums[index + 2] - 2:
            can3 = self.dfs(nums, index + 3, dp)

        dp[index] = 0
        if can1 or can2 or can3:
            dp[index] = 1

        return dp[index]

    def validPartition(self, nums):
        n = len(nums)
        dp = [-1] * (n + 1)

        return self.dfs(nums, 0, dp)
