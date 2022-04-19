class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for num in nums]
        for numIndex in range(len(nums)):
            currentNumber = nums[numIndex]
            currentIndex = numIndex
            #find the previous largest number and max length 
            longestOccurance = findLongestPrev(nums, currentNumber, currentIndex,dp)
            dp[numIndex] = longestOccurance + 1

            
        return max(dp)
def findLongestPrev(givenArray, currentNumber, currentIndex,dp):
    longestOccurance = 0 
    for i in range(currentIndex +1):
        if givenArray[i] < currentNumber:
            longestOccurance = max(longestOccurance, dp[i])
            
    return longestOccurance