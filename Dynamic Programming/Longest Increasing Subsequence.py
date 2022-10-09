class Solution:
    
    def lengthOfLIS(self, nums: List[int]) -> int:

        # well theres a binary search version but im not gonna break my head tonight lmao 
        # O(n^2) time and O(n) space complexity
        if len(set(nums)) == 1:
            return 1
        if not nums:
            return 0
        
        longest = [1] * len(nums)
        
        
        
        for index in range(1, len(nums)):
            currentNumber = nums[index] # my current Number 
            
            # find the number that is smaller than this and has the longest streak 
            longestStreak = 0
            smallest = float("-inf") # this number has to be smaller than the current Number 
            
            for j in range(index):
                if nums[j] < currentNumber and longest[j] > longestStreak:
                    longestStreak = longest[j]
                    
            longest[index] = longestStreak + 1

        return max(longest)