class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        currentPermutation = []
        
        getPermutations(nums, currentPermutation, permutations)
        
        return permutations
    
    
def getPermutations(givenArray, currentPermutation, permutations):
    if len(givenArray) == 0:
        permutations.append(currentPermutation)
        return 
    
    for numIndex in range(len(givenArray)):
            newArray = givenArray[:numIndex] + givenArray[numIndex+1:]
            newPermutation = currentPermutation + [givenArray[numIndex]]
            getPermutations(newArray, newPermutation, permutations)