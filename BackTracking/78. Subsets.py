class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        currentSet = []
        res.append(currentSet)
        for numIndex in range(len(nums)):
            currentNumber = nums[numIndex]
            for currentSetIndex in range(len(res)):
                res.append(res[currentSetIndex] + [currentNumber])
                
                
        return res