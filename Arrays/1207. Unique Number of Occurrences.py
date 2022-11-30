from collections import Counter 
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        myCount = Counter(arr)
        mySet = set()
        for key in myCount.values():
            if key in mySet:
                return False 
            
            mySet.add(key)
            
        return True 