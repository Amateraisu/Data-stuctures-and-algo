class Solution:
    def jump(self, nums: List[int]) -> int:
        #space is O(n) 
        # time complexity O(n^2)
        numberOfJumpsArray = [0 for num in nums]
        
        for i in reversed(range(len(nums)-1)):
            numberOfJump = findNumberOfJump(numberOfJumpsArray, nums, i)
            if nums[i] == 0:
                numberOfJumpsArray[i] = float("inf")
                continue
                
            numberOfJumpsArray[i] = numberOfJump + 1
        print(numberOfJumpsArray)
        return numberOfJumpsArray[0]
    
    
def findNumberOfJump(numberOfJumpsArray, nums, index):
    jumpableDistance = nums[index]
    windowIndexToConsider = min(index+jumpableDistance,len(nums)-1)
    minimum = float("inf")
    for i in range(index+1, windowIndexToConsider+1):

        minimum = min(numberOfJumpsArray[i],minimum)
    return minimum