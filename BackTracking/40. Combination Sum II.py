class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        currentCombination = []
        res = []
        candidates.sort()
        combinationSum2Helper(0, 0,currentCombination, res, target, candidates)
        
        return res
        
        
        
        
def combinationSum2Helper(currentSum, index, currentCombination, res, target, candidates):

    if currentSum > target:
        return 
    if currentSum == target:
        res.append(currentCombination)
        return 
    
    prev = - 1
    for i in range(index, len(candidates)):
        if candidates[i] == prev:
            continue
        newSum = currentSum + candidates[i]
        newCombination = currentCombination + [candidates[i]]
        combinationSum2Helper(newSum, i + 1, newCombination, res, target, candidates)
        prev = candidates[i]
        
    return