class Solution:
    def lengthLongestPath(self, directories: str) -> int:
        # "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

        
        
        
        splitted = directories.split("\n")

        stack = []

        for index in range(len(splitted)):
            countTabs, resString = count(splitted[index])

            splitted[index] = [resString, countTabs]
        res = 0 
        currentLength = 0
        
        for j in range(len(splitted)):
            
            while stack and stack[-1][1] >= splitted[j][1]:
                popped = stack.pop()
                currentLength -= len(popped[0])
                currentLength -= 1
            stack.append(splitted[j])
            currentLength += len(splitted[j][0])

            if isExtension(splitted[j][0]):
                res = max(res, currentLength)
                # print(splitted[j][0], "true", currentLength)

            currentLength += 1 
            # print(stack, res, currentLength)
        return res
    
    
    
    
def isExtension(string):

    if "." in string:
        return True 
    
    return False
            
def count(inputString):
    res = inputString.split("\t")
    counter = 0 
    for char in res:
        if char == "":
            counter += 1 
            
    return [counter, res[-1]]