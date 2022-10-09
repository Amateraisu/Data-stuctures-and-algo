class Solution:
    def partitionString(self, string: str) -> int:
        # partition the minimum number of substrings 
        # essentially I want to greed as many characters as possible 
        # I want to contain as many characters inside a substring as possible 
        
        res = 1
        mySet = set()
        for char in string:
            if char not in mySet:
                mySet.add(char)
                
            else:

                mySet = set()
                mySet.add(char)
                res += 1 
                
                
        return res
            