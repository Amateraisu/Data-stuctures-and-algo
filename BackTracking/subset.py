class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        currentSubset = []
        buildSubsets(currentSubset,0, res, nums)
        
        return res
        
def buildSubsets(currentSubset, index, res, nums):
    
    if index > len(nums):
        return
    res.append(currentSubset)
    
    for i in range(index, len(nums)):
        newArray = currentSubset + [nums[i]]

        buildSubsets(newArray,i + 1, res, nums)
        
        
    return