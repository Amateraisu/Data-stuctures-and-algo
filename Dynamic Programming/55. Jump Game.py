class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        isJumpable = [False for num in nums]
        isJumpable[-1] = True
        for i in reversed(range(0,len(nums)-1)):
            jumpableDistance = nums[i]
            possible = checkPossible(nums, i, isJumpable)
            if possible:
                # print("ran")
                isJumpable[i] = True
        # print(isJumpable)
        return isJumpable[0]
            
def checkPossible(numsArray, index, isJumpable):
    jumpableDistance = numsArray[index]
   
    jumpableIndex = min(len(numsArray)-1, index+jumpableDistance)
    # print(jumpableDistance, jumpableIndex, isJumpable)
    for i in range(index, jumpableIndex+1):
        # print("here", index, isJumpable)
        if isJumpable[i]:
            # print("here")
            return True
        
    return False