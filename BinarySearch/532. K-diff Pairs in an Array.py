class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        visited = set()
        for i in range(1, n):
            target = nums[i] - k
            l = bisect.bisect_left(nums, target)
            if nums[l] == target and l < i:
                visited.add((nums[l], nums[i]))

        return len(visited)