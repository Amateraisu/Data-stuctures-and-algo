class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        c1 = [1 for i in range(n)]
        c2 = [1 for i in range(n)]
        for i in range(n - 2, -1, -1):
            if nums1[i] <= nums1[i + 1]:
                c1[i] = max(c1[i], c1[i + 1] + 1)
            if nums1[i] <= nums2[i + 1]:
                c1[i] = max(c1[i], c2[i + 1] + 1)

            if nums2[i] <= nums1[i + 1]:
                c2[i] = max(c2[i], c1[i + 1] + 1)
            if nums2[i] <= nums2[i + 1]:
                c2[i] = max(c2[i], c2[i + 1] + 1)
        return max(max(c1), max(c2))