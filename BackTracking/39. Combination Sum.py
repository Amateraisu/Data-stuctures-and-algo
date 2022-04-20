class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        currentCombination = []
        
        getCombinations(candidates, currentCombination, combinations, target)
 
        return combinations



def getCombinations(candidates, currentCombination, combinations, target):
    if sum(currentCombination) > target:
        return 
    elif sum(currentCombination) == target:
        currentCombination.sort()
        if currentCombination not in combinations:
            combinations.append(currentCombination)
        return
    
    for candidate in candidates:
        newCombination = currentCombination + [candidate]
        getCombinations(candidates, newCombination, combinations, target)
    
    return 