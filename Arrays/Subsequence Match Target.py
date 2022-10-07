class Solution:
    def solve(self, words, s):


        # I can construct an array of hashmaps 

        mapArray = [{} for i in range(len(s))]
        # then go through the string s in reverse order 
        runningDict = {}
        for i in range(len(s) - 1, -1, -1):
            temp = runningDict.copy()
            mapArray[i] = temp
            runningDict[s[i]] = i + 1


        # also assign the first character 
        runningDict[s[0]] = 1 
        mapArray = [runningDict] + mapArray
        res = 0 
        # print(mapArray)
        for word in words:
            
            # check validity 
            if valid(word, mapArray):
                res += 1 
                print(word)
        
        return res 


def valid(word, mapArray):
    ptr1 = 0
    for char in word:
        if char not in mapArray[ptr1]:
            return False 
        else:
            ptr1 = mapArray[ptr1][char]
    return True
                







#         res = 0 
#         for word in words:
#             if isSubsequence(word, s):
#                 res += 1 

#         return res

# # O(MN) time complexity 

# # what if I straight away compute all possible subsequences of s?
 
# def isSubsequence(word, s):
#     ptr1 = 0 
#     ptr2 = 0 
#     for char in s:
#         if ptr1 < len(word) and char == word[ptr1]:
#             ptr1 += 1 

#     return ptr1 == len(word)