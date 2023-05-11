class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        m = len(nums1)
        n = len(nums2)
        @cache
        def dfs(i1, i2):
            if i1 == m or i2 == n:
                return 0
            best = 0
            # how do i decide how to connect a number ?
            #
            if nums1[i1] == nums2[i2]:
                best = max(best, dfs(i1 + 1, i2 + 1) + 1)
            else:
                best = max(best, dfs(i1 + 1, i2), dfs(i1, i2 + 1))

            return best

        return dfs(0, 0)