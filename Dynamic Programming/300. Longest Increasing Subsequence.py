class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longestSub = [1 for num in range(len(nums))]
        
        for index in range(1, len(nums)):
            #find the max subsequence of number before this 
            # number must be less than current number
            curNum = nums[index]
            maxOccur = findMaxOccur(index, curNum, longestSub, nums)
            
            # if max Occur is 0, dont do anything , else , use it + 1
            longestSub[index] = maxOccur + 1
            
        
        return max(longestSub)
            
            
            
def findMaxOccur(index, curNum, longestSub, nums):
    maximum = 0
    for currentIndex in range(index):
        currentNum = nums[currentIndex]
        currentMax = longestSub[currentIndex]
        if currentNum < curNum and currentMax > maximum:
            maximum = currentMax
        
    return maximum