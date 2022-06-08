


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {"1": [], "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        res = []
        currentCombinations = []
        startingIndex = 0
        letterCombinationsHelper(startingIndex, currentCombinations, res, dictionary, digits)
        
        return res
        
def letterCombinationsHelper(currentIndex, currentCombinations, res, dictionary, digits):
    if currentIndex >= len(digits):

        if currentCombinations:
            
            res.append("".join(currentCombinations))
        return 
    
    
    currentDigit = digits[currentIndex]
    availableAlphabets = dictionary[currentDigit]
    for j in availableAlphabets:
        newString = currentCombinations + [j]
        letterCombinationsHelper(currentIndex + 1, newString, res, dictionary , digits)
            
    return