class Solution:
    def rob(self, nums: List[int]) -> int:
        # O(n) time and O(n) space 
        
        # top down 
        cache = {}
        def dfs(currentIndex, didRobPrev):
            if currentIndex == len(nums):
                return 0 
            if (currentIndex, didRobPrev) in cache:
                return cache[(currentIndex, didRobPrev)]
            
            temp = 0 
            if not didRobPrev:
                #cannot rob this one 
                # rob this one 
                temp = max(dfs(currentIndex + 1, True) + nums[currentIndex], dfs(currentIndex + 1, False))
            else:
                # if did robPrev, cannot rob this 
                temp = max(temp, dfs(currentIndex + 1, False))
                
            cache[(currentIndex, didRobPrev)] = temp
            return cache[(currentIndex, didRobPrev)]
        
        return dfs(0, False)
    
    
    # bottom up 
    
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        dp = [0 for num in nums]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i] , dp[i - 1])
            
        return dp[-1]