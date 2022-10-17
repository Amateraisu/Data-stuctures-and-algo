class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0 
        left = 0 
        currentProd = 1 
        res = 0 
        for i, num in enumerate(nums):
            currentProd *= num 
            while currentProd >= k and left <= i:
                 
                
            
                currentProd /= nums[left]
                left += 1
            res += i - left + 1
                
                
            # print(i, left, "right, left")
            # print("result", res)
        return res