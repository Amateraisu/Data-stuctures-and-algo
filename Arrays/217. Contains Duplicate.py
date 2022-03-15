class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        
        for value in nums:
            if value not in hashmap:
                hashmap[value] = 1
            else:
                return True
            
            
        return False