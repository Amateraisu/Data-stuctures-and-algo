class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # [7, 8, 9, 11, 12]
        # I can set certain numbers
        # [7,8,9,11,12]
        # so I go through this array, and I can set the indexes in which they should be at
        # but if the number is huge, how do I handle that?
        # n = 5
        c = 0
        for num in nums:
            if num == 1:
                c += 1
        if not c:
            return 1
            # 7, 8, 9, 11, 12
        # I can just set the indexes, take the number and MOD it, if its already set, dont change it, '
        n = len(nums)
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = 1
        for i in range(n):
            if nums[i] <= n and nums[abs(nums[i]) - 1] > 0:  # if number within range and ,
                nums[abs(nums[i]) - 1] *= -1

                # print(nums)
        # [3,4,-1,1]
        # [3, 4, 1, 1] # finish cleaning up
        # [3, 4, -1, 1] # mark index 3 -1 = 2
        # [3, 4, -1, -1] # mark index 4 - 1 = 3
        # mark index 1 - 1 = 0

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
