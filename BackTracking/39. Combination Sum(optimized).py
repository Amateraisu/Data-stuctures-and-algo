        currentSum = 0 
        currentCandidates = []
        res = set()
        combinationSumHelper(currentSum, currentCandidates, res, candidates, target)
        
        return res
    
def combinationSumHelper(currentSum, currentCandidates, res, candidates, target):

    if currentSum > target:
        return 
    if currentSum == target:
        currentCandidates.sort()
        res.add(tuple(currentCandidates))
            
    
    for i in range(len(candidates)):
        newSum = currentSum + candidates[i]
        
        newCandidates = currentCandidates + [candidates[i]]
        
        combinationSumHelper(newSum, newCandidates, res, candidates, target)