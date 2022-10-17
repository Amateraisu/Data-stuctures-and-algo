class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] += nums[i] + prefix[i - 1]
            

        indexMap = {}
        res = 0
        for i in range(len(nums)):
            currentTarget = prefix[i] - k

            if prefix[i] == k:
                res = max(res, i + 1)
                
                
            if currentTarget in indexMap:
                res = max(res, i - indexMap[currentTarget])
            if prefix[i] not in indexMap:
                indexMap[prefix[i]] =  i 
            
        return res