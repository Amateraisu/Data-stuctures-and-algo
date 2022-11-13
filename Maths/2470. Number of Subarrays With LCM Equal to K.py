class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        
        ans = 0 
        for i in range(len(nums)): 
            val = 1
            for j in range(i, len(nums)): 
                val = lcm(val, nums[j])
                if val == k: ans += 1
        return ans 