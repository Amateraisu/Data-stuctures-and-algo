class Solution:
    def numWays(self, s: str) -> int:
        # so obviouslky what we want to do is have an equal amount of 1s in all the strings 
        count = getNumOnes(s)
        if count % 3 != 0:
            return 0 
        n = len(s)
        # try to split the string now 
        if count == 0:
            return ((n - 1) * (n - 2) // 2) % (10**9 + 7)
        validPartition = count / 3 
        left, right, count = 0 , 0 ,0
        # make it valid first, then count he number of 0s 
        for char in s:
            if char == "1":
                count += 1 
            if count == validPartition:
                left += 1 
            elif count == validPartition * 2:
                right += 1 
                
        return (left * right) % (10**9 + 7)

            
        
        
        
        
def getNumOnes(string):
    res = 0 
    
    for char in string:
        if char == "1":
            res += 1 
            
    return res