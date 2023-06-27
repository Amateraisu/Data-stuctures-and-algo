class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        res = r

        def valid(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k
        while l <= r:
            m = l + (r - l)//2
            print(m, "current")
            if valid(m):
                r = m - 1
                res = m
            else:
                l = m + 1
        return res