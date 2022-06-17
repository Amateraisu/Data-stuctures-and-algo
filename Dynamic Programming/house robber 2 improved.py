class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            return nums[0]
        firstHouses = nums[:-1]
        secondHouses = nums[1:]
        print(self.houseRobberHelper(firstHouses))
        print(self.houseRobberHelper(secondHouses))
        
        return max(self.houseRobberHelper(firstHouses), self.houseRobberHelper(secondHouses))
        
    def houseRobberHelper(self, houses):
        if len(houses) <= 2:
            return max(houses)
        dp = [0 for i in range(len(houses))]
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])
        for i in range(2, len(houses)):
            dp[i] = max(houses[i] + dp[i - 2], dp[i - 1])
            
        print(dp)
            
        return dp[-1]