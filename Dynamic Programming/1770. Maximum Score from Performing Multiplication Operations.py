class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        @cache
        def dfs(start, end, i):

            if i == len(multipliers):
                return 0
            if start > end:
                return 0
            best = float("-inf")

            best = max(best, dfs(start + 1, end, i + 1) + nums[start] * multipliers[i])
            best = max(best, dfs(start, end - 1 , i + 1) + nums[end] * multipliers[i])
            # print(start, end, i, best)
            return best

        return dfs(0, len(nums) - 1, 0)