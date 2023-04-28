class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot // 2 != tot / 2:
            return False

        target = tot // 2
        n = len(nums)

        @cache
        def dfs(currentIndex, currentNum):

            if currentNum == target:
                return True
            if currentIndex == n:
                return False

            if currentNum > target:
                return False

                # can choose to include or not to include
            if dfs(currentIndex + 1, currentNum):
                return True
            if dfs(currentIndex + 1, currentNum + nums[currentIndex]):
                return True

            return False