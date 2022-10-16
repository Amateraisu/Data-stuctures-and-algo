class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = 0
        last_min_k_index = -1
        last_max_k_index = -1
        fixed_bounds_subarrays = 0

        for right, v in enumerate(nums):
            if v < minK or v > maxK:
                left = right + 1
            else:
                if v == minK:
                    last_min_k_index = right
                if v == maxK:
                    last_max_k_index = right
                if last_min_k_index >= left and last_max_k_index >= left:
                    fixed_bounds_subarrays += min(last_min_k_index, last_max_k_index) - left + 1

        return fixed_bounds_subarrays