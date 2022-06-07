class Solution:
    def partition(self, string: str) -> List[List[str]]:
        currentPartitions = []
        res = []
        
        partitionsHelper(string, currentPartitions, res, 0)
        
        
        return res
    
def partitionsHelper(string, currentPartitions, res, currentIndex):

    if currentIndex >= len(string):

        res.append(currentPartitions)

        return 
    # 0, 1, 2 
    # e  ef efe
    for i in range(currentIndex, len(string)):
        currentString = string[currentIndex: i + 1]
        print(currentString , currentIndex, i + 1)
        # print(currentString)
        if isPalindrome(currentString):  
            newPartitions = currentPartitions + [currentString]
 
            partitionsHelper(string, newPartitions, res, i + 1)

        
            
    return


def isPalindrome(string):
    if len(string) == 1:
        return True 

    ptr1 = 0 
    ptr2 = len(string) - 1
    while ptr1 < ptr2:
        if string[ptr1] != string[ptr2]:
            return False 
        ptr1+=1
        ptr2-=1
    return True