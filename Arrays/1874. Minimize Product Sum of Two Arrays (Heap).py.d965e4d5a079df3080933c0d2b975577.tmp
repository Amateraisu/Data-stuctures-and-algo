class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        
        maxHeap = [-num for num in nums2]
        heapq.heapify(maxHeap)
        print(maxHeap)
        total = 0
        for ptr in range(len(nums2)):
            total += nums1[ptr] * heapq.heappop(maxHeap) * -1
        return total