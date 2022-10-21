class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myDict = {}
        
        
        for i, num in enumerate(nums):
            if num in myDict and i - myDict[num] <= k:
                return True 
            
            myDict[num] = i 
            
        return False